#!/usr/bin/python

# This script checks all security groups in our account for 0.0.0.0/0.
# We can extend this as necessary in the future.

import boto3
import json


def lambda_handler(json_input, context):
  ec2_client = boto3.client('ec2')
  sns_client = boto3.client('sns')
  sts_client = boto3.client('sts')
  response = ec2_client.describe_regions()
  region_list = []
  message = "OK"
  for region in response['Regions']:
    region_list.append(region['RegionName'])
  for region in region_list:
    ec2_client = boto3.client('ec2', region_name=region)
    response = ec2_client.describe_security_groups(
      Filters=[
        {
          'Name': 'ip-permission.cidr',
          'Values': ['0.0.0.0/0']
        }
      ]
    )
    if response['SecurityGroups'] != []:
      message = "The following security groups in {} have ports that are open to the world (0.0.0.0/0):\n".format(region)
    for security_group in response['SecurityGroups']:
      message += security_group['GroupId'] + '\n'
  if "OK" not in message:
    account = sts_client.get_caller_identity()['Account']
    accounts_dict = {
      '<account_number_1>': '<human-readable_account_name_1>', 
      '<account_number_2>': '<human-readable_account_name_2>'
    }
    sns_client.publish(
      Message=message,
      Subject = 'AWS Security Group Alert in {0} environment'.format(accounts_dict[account]),
      TopicArn='<topic_arn_to_send_alerts_to>'
    )
    return message
  else:
    message = 'No security groups need to be adjusted.'
    return message


if __name__ == '__main__':
  lambda_handler()
