import json
import boto3

client = boto3.client('s3')

def s3Upload(event, context):

    # Read File
    file_reader = open('source/data.txt').read()

    # Upload file to S3 Bucket
    upload_response = client.put_object(
        ACL='private',
        Body=file_reader,
        Bucket='pythondatademo123',
        Key='demo/data.txt'
    )

    # create a response to user
    response = {
        "statusCode": 200,
        "body": json.dumps(upload_response)
    }

    return response
