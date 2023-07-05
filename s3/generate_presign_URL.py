import boto3
s3 = boto3.client('s3')
  
  # Generate a presigned URL for the S3 object
s3_client = boto3.client('s3')
response = s3_client.generate_presigned_url('get_object', Params={'Bucket': "nbag-boto3-07022023", 'Key': "test_text.txt"}, ExpiresIn=300)
print(response)
        