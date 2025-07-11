import json
import boto3
import time
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FitnessWorkouts')

def lambda_handler(event, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }
    
    if event['httpMethod'] == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers}
    
    try:
        body = json.loads(event['body'])
        workout_id = f"{body['userId']}_{int(time.time() * 1000)}"
        
        item = {
            'workoutId': workout_id,
            'userId': body['userId'],
            'date': body['date'],
            'exercise': body['exercise'],
            'category': body['category'],
            'sets': body['sets'],
            'reps': body['reps'],
            'weight': [Decimal(str(w)) for w in body['weight']],
            'createdAt': str(int(time.time()))
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Workout created successfully',
                'workoutId': workout_id
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }