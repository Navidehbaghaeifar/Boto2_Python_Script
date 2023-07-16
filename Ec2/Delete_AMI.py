import boto3
ec2 = boto3.client('ec2')
response =ec2.deregister_image(ImageId='ami-0f4b862f4c20031c5')
