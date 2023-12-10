# app.py
from flask import Flask
from tablehandler import get_dynamodb_data

# AWS credentials and region configuration
aws_access_key = 'AKIAXCWMEHTAR4FWNARJ'
aws_secret_key = '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'
aws_region = 'eu-north-1'
table_name = 'Matrix_1'
# Initialize DynamoDB client

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, API status health is working fine'

@app.route('/MATRIX_1')
def matrix1():
    return get_dynamodb_data(aws_access_key, aws_secret_key, aws_region, 'MATRIX_1')

@app.route('/MATRIX_2')
def matrix2():
    return get_dynamodb_data(aws_access_key, aws_secret_key, aws_region, 'MATRIX_2')

@app.route('/MATRIX_3')
def matrix3():
    return get_dynamodb_data(aws_access_key, aws_secret_key, aws_region, 'MATRIX_3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
