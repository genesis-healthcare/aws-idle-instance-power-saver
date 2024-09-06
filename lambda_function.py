import boto3
import json
from resources import EC2_INSTANCES, ECS_CLUSTERS, RDS_INSTANCES, AURORA_CLUSTERS

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    ecs_client = boto3.client('ecs')
    rds_client = boto3.client('rds')

    action = event.get('action')

    if action == 'start':
        start_resources(ec2_client, ecs_client, rds_client)
    elif action == 'stop':
        stop_resources(ec2_client, ecs_client, rds_client)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid action provided. Use "start" or "stop".')
        }

    return {
        'statusCode': 200,
        'body': json.dumps(f'{action.capitalize()} action completed successfully.')
    }

def start_resources(ec2_client, ecs_client, rds_client):
    # Start EC2 instances
    if EC2_INSTANCES:
        ec2_client.start_instances(InstanceIds=EC2_INSTANCES)
        print(f'Started EC2 instances: {EC2_INSTANCES}')
    
    # Scale up ECS cluster services
    for cluster in ECS_CLUSTERS:
        services = ecs_client.list_services(cluster=cluster)['serviceArns']
        for service in services:
            ecs_client.update_service(cluster=cluster, service=service, desiredCount=1)
        print(f'Scaled up ECS cluster services: {cluster}')

    # Start RDS instances
    for db_instance in RDS_INSTANCES:
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

    # Start Aurora clusters
    for cluster in AURORA_CLUSTERS:
        try:
            rds_client.start_db_cluster(DBClusterIdentifier=cluster)
            print(f'Started Aurora cluster: {cluster}')
        except rds_client.exceptions.InvalidDBClusterStateFault as e:
            print(f"Error starting Aurora cluster {cluster}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error starting Aurora cluster {cluster}: {str(e)}")

def stop_resources(ec2_client, ecs_client, rds_client):
    # Stop EC2 instances
    if EC2_INSTANCES:
        ec2_client.stop_instances(InstanceIds=EC2_INSTANCES)
        print(f'Stopped EC2 instances: {EC2_INSTANCES}')
    
    # Scale down ECS cluster services
    for cluster in ECS_CLUSTERS:
        services = ecs_client.list_services(cluster=cluster)['serviceArns']
        for service in services:
            ecs_client.update_service(cluster=cluster, service=service, desiredCount=0)
        print(f'Scaled down ECS cluster services: {cluster}')

    # Stop RDS instances
    for db_instance in RDS_INSTANCES:
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

    # Stop Aurora clusters
    for cluster in AURORA_CLUSTERS:
        try:
            rds_client.stop_db_cluster(DBClusterIdentifier=cluster)
            print(f'Stopped Aurora cluster: {cluster}')
        except rds_client.exceptions.InvalidDBClusterStateFault as e:
            print(f"Error stopping Aurora cluster {cluster}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error stopping Aurora cluster {cluster}: {str(e)}")
