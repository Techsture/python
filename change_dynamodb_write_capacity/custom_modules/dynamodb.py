import boto3
import sys

""" Global Vars used by all functions """
regions = ["us-east-1", "us-west-1", "us-west-2"]
vpc_ids = { 'us-east-1' : 'vpc-9a80e1fe', 'us-west-1' : 'vpc-a66ce6c3', 'us-west-2' : 'vpc-53a69f36' }

def get_dynamodb_connection(region):
    conn = boto3.client('dynamodb', region)
    return conn

def get_table_read_capacity(conn, table_name):
    return conn.describe_table(TableName=table_name)['Table']['ProvisionedThroughput']['ReadCapacityUnits']

def get_table_write_capacity(conn, table_name):
    return conn.describe_table(TableName=table_name)['Table']['ProvisionedThroughput']['WriteCapacityUnits']

def set_table_write_capacity(conn, table_name, read_capacity, write_capacity):
    throughput_values = {}
    throughput_values['ReadCapacityUnits'] = int(read_capacity)
    throughput_values['WriteCapacityUnits'] = int(write_capacity)
    conn.update_table(TableName=table_name, ProvisionedThroughput=throughput_values)

