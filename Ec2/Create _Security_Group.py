import boto3
ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='Sg from Boto3',
    GroupName='Boto3-security-group',
    VpcId='vpc-0e3185f95739a1a24',
)

print(response["GroupId"])
