import boto3
import json

from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


def get_dynamodb_data(aws_access_key, aws_secret_key, aws_region, table_name):
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

    # Get the DynamoDB table
    table = dynamodb.Table(table_name)

    # Scan the table to retrieve all items
    response = table.scan()

    # Return the items as JSON
    items = response.get('Items', [])
    return json.dumps(items, cls=DecimalEncoder)




