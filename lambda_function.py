# This requests is an external dependency and is used to demonstrate 
# the demo of installing an external dependency in the lambda function.
import requests

#Lambda function execution begins from here.
def lambda_handler(event, context):
    print("Lambda Executed")
    print("This is a demo Lambda function")
    
    return 'Good Luck!'
