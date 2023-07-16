

import boto3
ec2 = boto3.client('ec2')
response = ec2.create_image(
    InstanceId=' i-0d5d09d3ba9d976f9',
    Name='Go To AMi',
   )

print(response["ImageId"])