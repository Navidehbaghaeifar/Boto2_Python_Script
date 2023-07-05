import boto3

s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket="nbag-boto3-07022023", Prefix = "folder /filder a/" )  
#response = s3.list_objects_v2(Bucket="nbag-boto3-07022023" )
for content in response["Contents"]:
    if (".txt" in content["Key"][-4:]):  #files contents has last txt(end with .txt)
     print(content["Key"])
    