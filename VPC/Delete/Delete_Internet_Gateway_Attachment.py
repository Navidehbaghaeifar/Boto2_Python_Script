import boto3
internet_gateway_id = "igw-0cadc2ca7a05bbb69"
vpc_id = "vpc-0f13b7feb2b26218a"
ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

