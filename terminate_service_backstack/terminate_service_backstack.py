#!/usr/bin/python

# This script terminates all EBStalk backstack instances.

from common_modules import asg
from common_modules import ebstalk


def main():
  asg_list = []
  regions = ["us-east-1", "us-west-1", "us-west-2"]
  # For each region, first create all of the connections, and then get a dict for all the AutoScaling
  #    Groups and EBStalk environemnts.
  for region in regions:
    asg_connection = asg.get_asg_connection(region)
    ebstalk_connection = ebstalk.get_ebstalk_connection(region)
    asg_dict = asg.get_all_groups(asg_connection)
    environment_dict = ebstalk.get_ebstalk_environments(ebstalk_connection)
    # Get the list of all the EBStalk backstack environment autoscaling groups.
    for environment in environment_dict['Environments']:
      if "back" in environment['CNAME']:
        resources = ebstalk.get_ebstalk_resources(ebstalk_connection, environment['EnvironmentName'])
        for backstack_asg in resources['EnvironmentResources']['AutoScalingGroups']:
          asg_list.append(backstack_asg['Name'])
    # For all of the Environment backstacks, set the capacity of their autoscaling groups to 0.
    for autoscaling_group in asg_dict['AutoScalingGroups']:
      if autoscaling_group['AutoScalingGroupName'] in asg_list:
        print(autoscaling_group['AutoScalingGroupName'])
        print(asg.update_capacity(asg_connection, autoscaling_group['AutoScalingGroupName'], 0))


if __name__ == "__main__":
  main()

