import json
import boto3

# create glue client
client=boto3.client('glue')

def lambda_handler(event, context):
    
    print('-------------------------------------')
    response = client.start_crawler(Name = 'imba raw data crawler')
    print(json.dumps(response,indent = 4))
    