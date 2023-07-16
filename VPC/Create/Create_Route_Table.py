import boto3
ec2 = boto3.client('ec2')
vpcId="vpc-0f13b7feb2b26218a"
routetable = ec2.create_route_table(VpcId=vpcId)
print(routetable["RouteTable"]["RouteTableId"])
