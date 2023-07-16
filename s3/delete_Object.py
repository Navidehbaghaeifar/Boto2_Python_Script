import boto3
s3=boto3.client('s3')
bucket= "nbag-boto3-07022023"
key = "test_text.txt"


response = s3.delete_object(
    Bucket=bucket,
    Key=key,
   )