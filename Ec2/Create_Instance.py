import boto3
ami_id = "ami-0f4b862f4c20031c5"
key_pair_name = "key from Boto3"
security_group_id = "sg-032ddadb3f83c1f99"
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id,
    ],
   
)
print(response["Instances"][0]["InstanceId"]) #validating first instances
