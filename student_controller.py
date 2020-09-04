import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

def get_items():
    table = dynamodb.Table('Student')
    try:
        table_content = table.scan()
    except Exception:
        return {
            "statusCode": 502,
            "headers": {},
            "body": "Error scanning table"
        }
    response = {
        "statusCode": 200,
        "body": (table_content['Items'])
    }
    return response