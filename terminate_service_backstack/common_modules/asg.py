import boto3

def get_asg_connection(region):
  conn = boto3.client('autoscaling', region_name=region)
  return conn

def get_all_groups(conn):
  response = conn.describe_auto_scaling_groups()
  return response

def update_capacity(conn, group_name, desired_instances):
  if desired_instances == 0:
    conn.update_auto_scaling_group(AutoScalingGroupName=group_name, MinSize=0)
    response = conn.set_desired_capacity(AutoScalingGroupName=group_name, DesiredCapacity=desired_instances)
  else:
    response = conn.set_desired_capacity(AutoScalingGroupName=group_name, DesiredCapacity=desired_instances)
  return response

