import boto3
vpc_id="vpc-0f13b7feb2b26218a"
ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
