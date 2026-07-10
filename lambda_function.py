# lambda_function.py
import boto3
import json
from resources import (
    EC2_INSTANCES,
    ECS_CLUSTERS,
    RDS_INSTANCES,
    AURORA_CLUSTERS,
    APP_RUNNER_SERVICES,
    ON_DEMAND_RESOURCES,
)

def filter_resources(resources, include_on_demand=False):
    filtered = []
    for r in resources:
        if not include_on_demand and r in ON_DEMAND_RESOURCES:
            continue
        filtered.append(r)
    return filtered

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    ecs_client = boto3.client('ecs')
    rds_client = boto3.client('rds')
    apprunner_client = boto3.client('apprunner')

    action = event.get('action')
    # include_on_demand: オンデマンドリソースも操作対象とするかどうか（デフォルトは False）
    include_on_demand = event.get('include_on_demand', False)

    if action == 'start':
        start_resources(ec2_client, ecs_client, rds_client, apprunner_client, include_on_demand)
    elif action == 'stop':
        stop_resources(ec2_client, ecs_client, rds_client, apprunner_client, include_on_demand)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid action provided. Use "start" or "stop".')
        }

    return {
        'statusCode': 200,
        'body': json.dumps(f'{action.capitalize()} action completed successfully.')
    }

def start_resources(ec2_client, ecs_client, rds_client, apprunner_client, include_on_demand):
    # EC2 の起動対象をフィルタリング
    target_ec2 = filter_resources(EC2_INSTANCES, include_on_demand)
    if target_ec2:
        ec2_client.start_instances(InstanceIds=target_ec2)
        print(f'Started EC2 instances: {target_ec2}')
    
    # ECS クラスターの対象をフィルタリングして、各クラスター内のサービス desiredCount を 1 に設定
    target_ecs = filter_resources(ECS_CLUSTERS, include_on_demand)
    for cluster in target_ecs:
        services = ecs_client.list_services(cluster=cluster)['serviceArns']
        for service in services:
            ecs_client.update_service(cluster=cluster, service=service, desiredCount=1)
        print(f'Scaled up ECS cluster services: {cluster}')

    # RDS インスタンスの起動（Aurora はクラスタ単位なので個別起動はスキップ）
    target_rds = filter_resources(RDS_INSTANCES, include_on_demand)
    for db_instance in target_rds:
        try:
            response = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance)
            db_instance_status = response['DBInstances'][0]['DBInstanceStatus']
            engine = response['DBInstances'][0]['Engine']
            if 'aurora' in engine:
                print(f"Skipping individual start for Aurora instance: {db_instance}")
                continue
            if db_instance_status == 'stopped':
                rds_client.start_db_instance(DBInstanceIdentifier=db_instance)
                print(f'Started RDS instance: {db_instance}')
            else:
                print(f'RDS instance {db_instance} is already in {db_instance_status} state.')
        except rds_client.exceptions.InvalidDBInstanceStateFault as e:
            print(f"Error starting RDS instance {db_instance}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error starting RDS instance {db_instance}: {str(e)}")

    # Aurora クラスターの起動
    target_aurora = filter_resources(AURORA_CLUSTERS, include_on_demand)
    for cluster in target_aurora:
        try:
            rds_client.start_db_cluster(DBClusterIdentifier=cluster)
            print(f'Started Aurora cluster: {cluster}')
        except rds_client.exceptions.InvalidDBClusterStateFault as e:
            print(f"Error starting Aurora cluster {cluster}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error starting Aurora cluster {cluster}: {str(e)}")

    # App Runner サービスの再開
    target_apprunner = filter_resources(APP_RUNNER_SERVICES, include_on_demand)
    for service_arn in target_apprunner:
        try:
            apprunner_client.resume_service(ServiceArn=service_arn)
            print(f'Resumed App Runner service: {service_arn}')
        except Exception as e:
            print(f"Error resuming App Runner service {service_arn}: {str(e)}")

def stop_resources(ec2_client, ecs_client, rds_client, apprunner_client, include_on_demand):
    # EC2 の停止対象をフィルタリング
    target_ec2 = filter_resources(EC2_INSTANCES, include_on_demand)
    if target_ec2:
        ec2_client.stop_instances(InstanceIds=target_ec2)
        print(f'Stopped EC2 instances: {target_ec2}')
    
    # ECS クラスターの対象をフィルタリングして、各サービス desiredCount を 0 に設定
    target_ecs = filter_resources(ECS_CLUSTERS, include_on_demand)
    for cluster in target_ecs:
        services = ecs_client.list_services(cluster=cluster)['serviceArns']
        for service in services:
            ecs_client.update_service(cluster=cluster, service=service, desiredCount=0)
        print(f'Scaled down ECS cluster services: {cluster}')

    # RDS インスタンスの停止
    target_rds = filter_resources(RDS_INSTANCES, include_on_demand)
    for db_instance in target_rds:
        try:
            response = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance)
            db_instance_status = response['DBInstances'][0]['DBInstanceStatus']
            engine = response['DBInstances'][0]['Engine']
            if 'aurora' in engine:
                print(f"Skipping individual stop for Aurora instance: {db_instance}")
                continue
            if db_instance_status == 'available':
                rds_client.stop_db_instance(DBInstanceIdentifier=db_instance)
                print(f'Stopped RDS instance: {db_instance}')
            else:
                print(f'RDS instance {db_instance} is already in {db_instance_status} state.')
        except rds_client.exceptions.InvalidDBInstanceStateFault as e:
            print(f"Error stopping RDS instance {db_instance}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error stopping RDS instance {db_instance}: {str(e)}")

    # Aurora クラスターの停止
    target_aurora = filter_resources(AURORA_CLUSTERS, include_on_demand)
    for cluster in target_aurora:
        try:
            rds_client.stop_db_cluster(DBClusterIdentifier=cluster)
            print(f'Stopped Aurora cluster: {cluster}')
        except rds_client.exceptions.InvalidDBClusterStateFault as e:
            print(f"Error stopping Aurora cluster {cluster}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error stopping Aurora cluster {cluster}: {str(e)}")

    # App Runner サービスの一時停止
    target_apprunner = filter_resources(APP_RUNNER_SERVICES, include_on_demand)
    for service_arn in target_apprunner:
        try:
            apprunner_client.pause_service(ServiceArn=service_arn)
            print(f'Paused App Runner service: {service_arn}')
        except Exception as e:
            print(f"Error pausing App Runner service {service_arn}: {str(e)}")

