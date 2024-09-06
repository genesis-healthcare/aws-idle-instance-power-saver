# AWS Idle Instance Power Saver

## Overview

The **AWS Idle Instance Power Saver** is a serverless Lambda function written in Python that automatically starts and stops AWS resources like EC2, ECS, and RDS instances based on a defined schedule. This function helps reduce costs by powering down idle resources during non-business hours and restarting them during business hours.

You can trigger this Lambda function using AWS CloudWatch Events (cron jobs), specifying the action (`start` or `stop`) as a payload in the form of a JSON object.

## Features

- **Cost Optimization**: Automatically stop instances when not in use to reduce AWS costs.
- **Supports EC2, ECS, and RDS**: Manage EC2 instances, ECS clusters, RDS databases, and Aurora clusters.
- **Simple Configuration**: Trigger actions (`start` or `stop`) based on cron schedules.
- **Customizable**: Easy to modify for additional instance types or custom logic.

## Usage

### Prerequisites
- AWS Lambda setup with necessary permissions (EC2, ECS, RDS, Aurora).
- AWS CloudWatch for scheduling the Lambda function using cron expressions.

### Deployment

1. **Clone the repository**:
    ```bash
    git clone https://github.com/genesis-healthcare/aws-idle-instance-power-saver.git
    ```

2. **Deploy the Lambda function** (assuming usage of AWS SAM or Serverless Framework):
    ```bash
    sam deploy --guided
    ```

3. **Set up AWS CloudWatch Events**:
   Create CloudWatch cron events to trigger the Lambda function at the start and end of your business hours. Below are examples of JSON payloads:

   - To stop resources at the end of the business day:
     ```json
     {
       "action": "stop"
     }
     ```

   - To start resources at the beginning of the business day:
     ```json
     {
       "action": "start"
     }
     ```

### Example CloudWatch Event Rule

To stop instances every day at 6 PM, use the following cron expression in CloudWatch Events:

```
cron(0 18 ? * MON-FRI *)
```

To start instances every day at 8 AM:

```
cron(0 8 ? * MON-FRI *)
```

### Configuration

The Lambda function checks which AWS resources need to be stopped or started based on the JSON payload provided at runtime. Make sure to edit the Lambda function to include the list of instances, ECS clusters, and RDS/Aurora databases you want to manage.

### JSON Payload Example

```json
{
  "action": "start"
}
```

The valid actions are:

start: To start EC2, ECS, and RDS instances, and Aurora clusters.
stop: To stop EC2, ECS, and RDS instances, and Aurora clusters.

## Permissions

Ensure that your Lambda function has the necessary permissions to manage EC2 instances, ECS clusters, and RDS/Aurora databases. The policy should include actions like:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ecs:ListServices",
                "ecs:UpdateService",
                "ec2:StartInstances",
                "ec2:StopInstances",
                "rds:StartDBInstance",
                "rds:StopDBInstance",
                "rds:StartDBCluster",
                "rds:StopDBCluster",
                "rds:DescribeDBInstances"
            ],
            "Resource": "*"
        }
    ]
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
