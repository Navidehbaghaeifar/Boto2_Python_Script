import json
import boto3
from datetime import datetime

current_date_time = datetime.now()
sqs = boto3.resource('sqs', region_name='us-east-1')

def lambda_handler(event, content):
    
    queue = sqs.get_queue_by_name(QueueName='ProjectSqs') #get the queue

    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S") #get the current date and time
    message = ("The current date and time at point of trigger was " + str(date_time) + ".") # Create a custom message with the current date and time
    
    # Send the message to the queue
    responce = queue.send_message(MessageBody = message) 
# Return the response status code and message body
    return {
        "statusCode": 200,
        'body': json.dumps(message)
    }











