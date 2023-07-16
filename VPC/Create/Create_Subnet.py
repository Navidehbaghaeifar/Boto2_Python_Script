import boto3

cider_block = '12.0.1.0/24'
vpc_id = 'vpc-0f13b7feb2b26218a'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cider_block,VpcId=vpc_id)

print(subnet["Subnet"],["SubnetId"]) #output get one object