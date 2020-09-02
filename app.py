import boto3
import json
from flask import Flask
app = Flask(__name__)

dynamodb = boto3.client('dynamodb', region_name='eu-west-1')

@app.route("/")
def return_table_info():
      table = dynamodb.Table('Student')
      table_content = table.scan(
          TableName='Student',
          Select='ALL_ATTRIBUTES'
          )
      response = {
          "statusCode": 200,
          "body": json.dumps(table_content['Items'][0])
      }
      return response

print("Ajettu")