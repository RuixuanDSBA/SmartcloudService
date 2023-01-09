import boto3 
import time
import json


def lambda_handler(event, context):
    client = boto3.client('sagemaker')
    
    #wish to get current status of instance
    status = client.describe_notebook_instance(NotebookInstanceName='xgboost-ml')
    
    #Start the instance
    
    client.start_notebook_instance(NotebookInstanceName='xgboost-ml')

    #this lambda just trigger start_notebook_instance in sagemaker, but it doesn't decide which .py file to execute in the     #notebook_instance,
    #we need to config life-cycle item in sagemaker and conbine the item to which notebook-instance we run. 
     