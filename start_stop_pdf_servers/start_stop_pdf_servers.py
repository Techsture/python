#!/usr/bin/python

# This script will start and stop ds-pdf-live-ubuntu instances
# It accepts one parameter:
#   --activity [start | stop]
#
# The intention is that this script is run from a Jenkins job that triggers off a time-based schedule.


import argparse
from custom_modules import ec2, elb
import subprocess
import time


def start_servers(ec2_connection, elb_connection):
  # Start all the stopped "ds-pdf-live-ubuntu" instances.
  #   Right now the ds-pdf-live-ubuntu servers are only in us-west-2 on the Production account,
  #   so the region sent to the function is hardcoded here, along with the instance Name tag:
  all_pdf_instances = ec2.get_instances_by_tag_name(ec2_connection, "us-west-2", "ds-pdf-live-ubuntu")
  instance_ids = []
  for instance in all_pdf_instances:
    if instance['State']['Name'] == "stopped":
      instance_ids.append(instance['InstanceId'])
  ec2.start_instances(ec2_connection, instance_ids)
  # Wait 60 seconds for the instance DNS address and SSH to be ready.
  time.sleep(60)
  # Start the Tomcat process on all of the servers after they come up.
  public_dns = ec2.get_public_dns_by_instance_id(ec2_connection, "us-west-2", instance_ids)
  for address in public_dns:
      subprocess.Popen(["ssh", "ubuntu@%s" % address, "sudo /var/local/apache-tomcat-8.0.32/bin/startup.sh"])
  # Add the servers to the load balancer.
  elb.add_instances_to_elb(elb_connection, "ds-pdf-live-ubuntu", instance_ids)
  return


def stop_servers(ec2_connection, elb_connection):
  # Choose 19 instances and remove them from the load balancer (to leave a total of 5 remaining)
  #   TODO: This is not being done as efficiently as it probably can be since I'm tired.
  all_instances = ec2.get_instances_by_tag_name(ec2_connection, "us-west-2", "ds-pdf-live-ubuntu")
  stop_list = []
  instance_ids = []
  for i in range(0, 19):
      stop_list.append(all_instances.pop())
  for instance in stop_list:
      instance_ids.append(instance['InstanceId'])
  elb.remove_instances_from_elb(elb_connection, "ds-pdf-live-ubuntu", instance_ids)
  # Wait 30 seconds for all processing on the instances to end
  time.sleep(30)
  # Stop the instances
  ec2.stop_instances(ec2_connection, instance_ids)
  return


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--activity", help="start or stop", type=str, choices=["start", "stop"], required=True)
  args = parser.parse_args()
  # Create the EC2 connection.  Right now the ds-pdf-live-ubuntu servers are only in us-west-2, so the region sent
  # to the function is hardcoded here:
  ec2_connection = ec2.get_ec2_connection("us-west-2")
  elb_connection = elb.get_elb_connection("us-west-2")
  # Call the correct function based on the argument passed:
  if args.activity == "start":
    start_servers(ec2_connection, elb_connection)
  else:
    stop_servers(ec2_connection, elb_connection)
  exit()

if __name__ == "__main__":
  main()

