import boto3
route_table_id = 'rtb-0262683f5b82a2bbe'
internet_gateway_id = 'igw-0cadc2ca7a05bbb69'
ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)


