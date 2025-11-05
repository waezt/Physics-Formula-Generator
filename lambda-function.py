import boto3
import random
import json

print('Loading function')

#Initialise table from DynamoDB
dynamodb = boto3.resource('dynamodb')   
table = dynamodb.Table('Physics-Formulas')  

def get_random_formula():
    '''
    Return random formula from DynamoDB
    '''
    scanned_data = table.scan()
    print(scanned_data)  

    items = scanned_data.get('Items', [])
    if not items:
        return {"formula": "No formulas found", "explanation": ""}    #Message if table is empty

    random_item = random.choice(items)    #Select random formula
    return {
        "formula": random_item.get('Formula', ''),
        "explanation": random_item.get('Explanation', '')
    }

def lambda_handler(event, context):
    '''
    Lambda entry point, returns formula as JSON
    '''
    result = get_random_formula()
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*' 
        },
        'body': json.dumps(result)    #Convert to JSON string
    }

