import boto3
subnet_id = "subnet-095610a1890d458b3"
ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)
