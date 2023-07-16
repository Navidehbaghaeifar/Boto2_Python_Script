import boto3
route_table_id = 'rtb-0262683f5b82a2bbe'
subnet_id = 'subnet-095610a1890d458b3'
ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])
