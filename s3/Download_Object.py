import boto3
s3 = boto3.resource('s3')
s3.download_file('nbag-boto3-07022023', 'test_text.txt', 'test_text.txt')
