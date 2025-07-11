# 🔧 AWS Console Setup Guide

This guide shows the exact AWS console configurations used in this project.

## DynamoDB Table Setup
![DynamoDB Configuration](../screenshots/aws-console/dynamodb-table.png)

**Configuration:**
- Table name: `FitnessWorkouts`
- Partition key: `workoutId` (String)
- Billing mode: On-demand
- Encryption: AWS managed keys

## Lambda Functions Configuration
![Lambda Functions](../screenshots/aws-console/lambda-functions-list.png)

**Settings for all functions:**
- Runtime: Python 3.12
- Architecture: x86_64
- Timeout: 30 seconds
- Memory: 128 MB

![Lambda Permissions](../screenshots/aws-console/lambda-permissions.png)

**Required IAM Policy:**
- AWSLambdaBasicExecutionRole
- DynamoDBFullAccess

## API Gateway Configuration
![API Gateway Structure](../screenshots/aws-console/api-gateway-overview.png)

**Resource Structure:**
```
/
└── workouts
    ├── GET (→ GetWorkouts)
    ├── POST (→ CreateWorkout)
    └── {workoutId}
        └── DELETE (→ DeleteWorkout)
```

![CORS Configuration](../screenshots/aws-console/api-gateway-cors.png)

**CORS Settings:**
- Access-Control-Allow-Origin: *
- Access-Control-Allow-Headers: Content-Type
- Access-Control-Allow-Methods: GET,POST,DELETE,OPTIONS

## S3 Static Website Hosting
![S3 Configuration](../screenshots/aws-console/s3-bucket-overview.png)

**Bucket Settings:**
- Static website hosting: Enabled
- Index document: index.html
- Public access: Enabled
- Bucket policy: Public read access

![Website Hosting](../screenshots/aws-console/s3-website-hosting.png)