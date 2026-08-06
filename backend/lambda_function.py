import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-2')
    table = dynamodb.Table('visitor-count')
    
    response = table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='ADD #count :increment',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':increment': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    count = int(response['Attributes']['count'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': count})
    }