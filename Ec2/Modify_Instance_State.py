import boto3
instance_id = "i-0ac08b35d16465c42"

def stop_instance(client,instance_id):
    response = ec2.stop_instances(
        InstanceIds=[instance_id],
    )
    print(instance_id,"stopped")

def start_instance(client,instanceid):
    response = client.start_instances(
         InstanceIds=[instance_id],
    )
print(instance_id,"started")
def terminate_instance(client,instanceid):
    response = client.terminate_instances(
        InstanceIds=[instance_id],
)
print(instance_id,"terminated")

if __name__ == '__main':
    instance_id = "i-0ac08b35d16465c42"
ec2 = boto3.client('ec2')
terminate_instance(ec2,instance_id)  #we can startr,terminate and stop_instance and check in console is start,terminate,stops.




