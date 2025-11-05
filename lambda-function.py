import boto3
import random
import json

print('Loading function')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Physics-Formulas')  

def get_random_formula():
    scanned_data = table.scan()
    print(scanned_data)  

    items = scanned_data.get('Items', [])
    if not items:
        return {"formula": "No formulas found", "explanation": ""}

    random_item = random.choice(items)
    return {
        "formula": random_item.get('Formula', ''),
        "explanation": random_item.get('Explanation', '')
    }

def lambda_handler(event, context):
    result = get_random_formula()
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  
        },
        'body': json.dumps(result)
    }

