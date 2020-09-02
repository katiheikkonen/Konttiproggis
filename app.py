import boto3
import json
from flask import Flask
app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

@app.route("/")
def return_table_info():
      table = dynamodb.Table('Student')
      table_content = table.scan(
          TableName='Student',
          Select='ALL_ATTRIBUTES'
          )
      response = {
          "statusCode": 200,
          "body": json.dumps(table_content['Items'])
      }
      return response

print("Ajettu")