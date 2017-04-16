#!/usr/bin/python

# This script will scale DynamoDB write capacity up or down.
# It accepts three parameters:
#   --region [us-west-1 | us-east-1 | us-west-2]
#   --table_name [name]
#   --write_capacity [integer]
#
# The intention is that this script is run from a Jenkins job that triggers off a time-based schedule.


import argparse
from custom_modules import dynamodb
import subprocess


def main():
  # First, parse all the arguments:
  parser = argparse.ArgumentParser()
  parser.add_argument("--region", help="AWS region", type=str, choices=["us-east-1", "us-west-1", "us-west-2"], required=True)
  parser.add_argument("--table_name", help="DynamoDB table name", type=str, required=True)
  parser.add_argument("--write_capacity", help="table write capacity", type=str, required=True)
  args = parser.parse_args()
  # We don't want to change the ReadCapacityUnits, so we should get that from AWS directly.
  dynamodb_connection = dynamodb.get_dynamodb_connection(args.region)
  read_capacity = dynamodb.get_table_read_capacity(dynamodb_connection, args.table_name)
  # Set the write capacity:
  dynamodb.set_table_write_capacity(dynamodb_connection, args.table_name, read_capacity, args.write_capacity)


if __name__ == "__main__":
  main()

