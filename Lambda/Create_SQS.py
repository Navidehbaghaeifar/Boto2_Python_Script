
# Import the Boto3 library
import boto3

# Connect to the SQS
sqs = boto3.resource('sqs')

# put name of the queue
queue_name = 'ProjectSqs'

# Create the queue
queue = sqs.create_queue(QueueName=queue_name)

#print the URL of the created Amazon SQS queue
print(queue.url)
