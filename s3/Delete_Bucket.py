import boto3
s3=boto3.client('s3')
bucket = 'prodnavi'
response = s3.delete_bucket(
    Bucket=bucket,
    ExpectedBucketOwner='string'
)