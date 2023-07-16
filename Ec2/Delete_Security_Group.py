import boto3
ec2 = boto3.client('ec2')

response = ec2.delete_security_group(GroupId='sg-0e2eb71128d6d0450')

print(response)
