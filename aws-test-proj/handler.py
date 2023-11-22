import json
import boto3
import os
import uuid
import logging

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['DYNAMODB_TEST_TABLE'])

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello(event, context):
    
    key = str(uuid.uuid1())
    item = {
        'primary_key': key
    }
    
    response = table.put_item(Item=item)
    logger.info('## RESPONSE')
    logger.info(response)
    return {
        "status": 200,
    }


# https://swizec.com/blog/using-dynamodb-streams-with-the-serverless-framework/
# https://stackoverflow.com/questions/37703609/using-python-logging-with-aws-lambda
# https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python
# https://stackoverflow.com/questions/40937512/how-to-access-an-aws-lambda-environment-variable-from-python
# 