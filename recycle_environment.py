#!/usr/bin/env python

""" This script recycles all of the instances in a given environment.
It takes two required arguments: environment name and sleep time between instance terminations (in seconds).
It takes option arguments: instance IDs to ignore during recycling.

TODO: Right now this is just calling some of the Bash scripts that exist, only because I'm transliterating
this from another Bash script.  It should be using Boto. This is a problem because for a lot of these I had to
use 'shell=True', which is a security risk (shell injection). There's some other dumb things going on due to this
as well.  Welcome to Trump's America... """

import argparse
"""from subprocess import call """
from subprocess import call, check_output
import json
import requests
from datetime import datetime, timedelta
import time


def create_maintenance_window(environment_name):
  url = 'https://devero.pagerduty.com/api/v1/maintenance_windows'
  api_access_key = 'bz-c7zRWDhDxSF9GtywN'
  service_ids = ['PYGEN3X']
  """ Get the current time in PagerDuty-friendly UTC offset time format (<YYYY>-<MM>-<DD>T<hh>:<mm>:<ss>-<oo:oo>Z): """
  start_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
  """ Calculate the end time: """
  """ Set the window for six hours, which should be enough time... we'll be deleting it at the end of this script anyways.
    There may be instances in the future where we'll need a window longer than six hours to complete this, depending on
    sleep time and number of instances.  In that case, just increase the number of hours below. """
  end_time = (datetime.utcnow() + timedelta(hours=6)).strftime("%Y-%m-%d %H:%M:%SZ")
  """ Create the JSON to send to PagerDuty """
  headers = {
        'Authorization': 'Token token={0}'.format(api_access_key),
        'Content-type': 'application/json',
  }
  payload = {
      "maintenance_window": {
          'start_time': start_time,
          'end_time': end_time,
          "description": 'Maintenance mode for recycling {0}.'.format(environment_name),
          "service_ids": service_ids,
      }
  }
  request = requests.post(url, headers=headers, data=json.dumps(payload))
  parsed_response = json.loads(request.text)
  print(json.dumps(parsed_response, indent=2))
  return parsed_response['maintenance_window']['id']


def delete_maintenance_window(maintenance_id):
  url = 'https://devero.pagerduty.com/api/v1/maintenance_windows'
  api_access_key = 'bz-c7zRWDhDxSF9GtywN'
  headers = {
        'Authorization': 'Token token={0}'.format(api_access_key),
        'Content-type': 'application/json',
  }
  request = requests.delete(url + '/' + maintenance_id, headers=headers)
  print(request.text)
  print("Deleted PagerDuty maintenance window %s for Unhealthy Host Count service." % maintenance_id)


def recycle_instances(environment_name, live_environment, ignore_list, sleep_time):
  """ Get the region for the requested application """
  cmd = ['/jenkins/scripts/amazon/ebstalk/get_region.sh', environment_name ]
  region = str(check_output(cmd).split()[0])
  """ Get the list of instances """
  cmd = 'aws ec2 describe-instances --region ' + region + ' --filters "Name=tag:Name,Values=' + live_environment + '" | grep InstanceId | awk \'{print $2}\' | tr -d \'\"\' | tr -d \',\''
  instance_list = (check_output(cmd, shell=True).split())
  """ Get load balancer name """
  cmd = 'aws elasticbeanstalk describe-environments --region ' + region + ' --environment-names ' + live_environment + ' | grep EndpointURL | awk \'{print $2}\' | tr -d \'\"\' | tr -d \',\' | cut -d \'-\' -f 1-5'
  """ TODO: This is stupid.  The load balancer is being returned with an extra newline at the end. """
  load_balancer_name = (check_output(cmd, shell=True).rstrip())
  """ Remove each instance one-by-one with a wait in between each. """
  for instance in instance_list:
    """ If the ignore list is populated and the current instance is in said list, ignore it. """
    if ignore_list and (instance in ignore_list):
        print("Skipping this instance (%s) because we're testing leaving it up!" % instance)
    else:
        print("Removing instance %s from load balancer %s." % (instance, load_balancer_name))
        cmd = 'aws elb deregister-instances-from-load-balancer --region ' + region + ' --load-balancer-name ' + load_balancer_name + ' --instances ' + instance
        call(cmd, shell=True)
        print("Sleeping for 30s to ensure the instance is not getting anymore traffic.")
        time.sleep(30)
        print("Terminating instance %s..." % instance)
        cmd = 'aws ec2 terminate-instances --region ' + region + ' --instance-ids ' + instance
        call(cmd, shell=True)
        print("Sleeping for %ss before moving on to the next instance." % sleep_time)
        time.sleep(sleep_time)
  print("Done rebooting instances.")


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("environment_name", help="Environment name.", type=str)
  parser.add_argument("sleep_time", help="Time to sleep in between each termination.", type=int)
  parser.add_argument("--ignore", help="List of instance IDs to ignore.", nargs='*', type=str, required=False)
  args = parser.parse_args()
  """ Get the live environment for the requested application """
  cmd = ['/jenkins/scripts/amazon/ebstalk/get_environment.sh', args.environment_name, '--live']
  live_environment = str((check_output(cmd).split())[2])
  maintenance_id = create_maintenance_window(args.environment_name)
  recycle_instances(args.environment_name, live_environment, args.ignore, args.sleep_time)
  delete_maintenance_window(maintenance_id)


if __name__ == "__main__":
  main()
