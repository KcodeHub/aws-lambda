# Serverless Lambda

This example demonstrates how to upload File to S3 Bucket and Process the S3 File uploaded by triggering Lambda on File Creation to S3 Bucket.
It uses Serverless npm package to deploy Lambda into AWS with all the infrastructure creation.

## Use-cases

- API for a S3 File Upload
- Post Process Lambda which is executed and prints file content to CloudWatch

## Pre-Requisite
- Install Nodejs and npm to your host operating system
- Setup AWS CLI with user Secret Key to create resource in AWS.

## Setup

Install Serverless using below command after installing nodejs and npm. 

```bash
npm install -g serverless
```

## Deploy

In order to deploy the Lambda simply execute

```bash
serverless deploy
```

Deploy to specific stage or region. Ex.
```
serverless deploy --stage production --region us-east-1
```

The expected result should be similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service s3-upload-postprocess-lambda.zip file to S3 (6.38 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
....................
Serverless: Stack update finished...
Service Information
service: s3-upload-postprocess-lambda
stage: dev
region: us-east-1
stack: s3-upload-postprocess-lambda-dev
resources: 17
api keys:
  None
endpoints:
  POST - https://XXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/s3Upload
functions:
  postprocess: s3-upload-postprocess-lambda-dev-postprocess
  create: s3-upload-postprocess-lambda-dev-create
layers:
  None
```

## Usage

You can upload File using below command:

### Upload File to S3 Bucket

Run below command from terminal or AWS CLI to Upload File to S3 Bucket.

```bash
curl -X POST https://XXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/s3Upload --data '{ "text": "TEST Run" }'
```
#### output
```
{"ResponseMetadata": {"RequestId": "F8DD225D28F93E74", "HostId": "nkBjLrWRaBFMMyDZ0drnVwc098M+YkVgi+AvMlQMRFhPypg1sO8pN3APftYwkbF/ppvZYJ10cPo=", 
"HTTPStatusCode": 200, "HTTPHeaders": {"x-amz-id-2": "nkBjLrWRaBFMMyDZ0drnVwc098M+YkVgi+AvMlQMRFhPypg1sO8pN3APftYwkbF/ppvZYJ10cPo=", 
"x-amz-request-id": "F8DD225D28F93E74", "date": "Mon, 11 May 2020 18:21:28 GMT", "etag": "\"d771b080a8e114b9d7ef75ae55fc2c3c\"", 
"content-length": "0", "server": "AmazonS3"}, "RetryAttempts": 
```

## Undeploy

Use below command to Undeploy resources.

```
serverless remove --stage dev --region us-east-1
```