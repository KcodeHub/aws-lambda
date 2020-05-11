import boto3
client = boto3.client('s3')

# This Function will Read File from S3 Bucket whenever any file with .txt extension is created in S3
# Bucket - pythondatademo123
# Region - us-east-1

def file_handler(event, context):

    # Read data from S3 Bucket
    data = client.get_object(
        Bucket='pythondatademo123',
        Key='demo/data.txt'
    )

    contents = data['Body'].read()

    # Print data to Log - CloudWatch
    print(contents)
