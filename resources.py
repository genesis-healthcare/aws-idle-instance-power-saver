# Define the list of EC2 instance IDs that should be managed by the Lambda function.
# Replace these IDs with your actual EC2 instance IDs in the AWS environment.
EC2_INSTANCES = [
    "i-xxxxxxxxxxxxxxxxx",  # Example EC2 instance ID 1
    "i-yyyyyyyyyyyyyyyyy",  # Example EC2 instance ID 2
]

# Define the list of ECS cluster names that should be managed by the Lambda function.
# Replace these names with the actual ECS cluster names you want to start/stop.
ECS_CLUSTERS = [
    "ExampleECSCluster1",   # Example ECS Cluster 1
    "ExampleECSCluster2",   # Example ECS Cluster 2
]

# Define the list of RDS instance identifiers that should be managed by the Lambda function.
# Replace these identifiers with the actual RDS instance names.
RDS_INSTANCES = [
    "example-rds-instance-1",   # Example RDS Instance 1
    "example-rds-instance-2",   # Example RDS Instance 2
]

# Define the list of Aurora cluster identifiers that should be managed by the Lambda function.
# Replace these identifiers with the actual Aurora cluster names.
AURORA_CLUSTERS = [
    "example-aurora-cluster-1",  # Example Aurora Cluster 1
    "example-aurora-cluster-2",  # Example Aurora Cluster 2
]
