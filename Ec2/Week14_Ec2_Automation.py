import boto3
ami_id = "ami-06ca3ca175f37dd66"
key_pair_name = "keypairnew"
security_group_id = "sg-032ddadb3f83c1f99"
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=3,
    MinCount=3,
    SecurityGroupIds=[
        security_group_id,
    ],
   TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Environment',
                    'Value': 'Dev',
                },
            ],
        },
    ],
)
print(response["Instances"][0]["InstanceId"]) #validating first instances