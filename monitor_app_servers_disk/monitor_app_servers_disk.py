#!/usr/bin/python

# This script checks the root drive remaining space on all Staging and Production app servers.
# It's triggered via a Jenkins job.
# 1.) Get list of servers
# 2.) Get disk space remaining on root partition of each server
# 3.) If disk usage is over 85%, fail the Jenkins job.


from devero import ec2
import json
import subprocess
import sys

def main():
    aws_east1_conn = ec2.get_ec2_connection('us-east-1')
    aws_west1_conn = ec2.get_ec2_connection('us-west-1')
    # TODO: Programmatically figure out the stack names.  Don't have time for that right now.
    east1_stacks = [ 'p2', 'p4', 'p6', 's2', 's4' ]
    west1_stacks = [ 'p1', 'p5' ]
    failure_flag = False
    for stack in east1_stacks:
        stack_dns_names = ec2.get_public_dns_by_tag_name(aws_east1_conn, 'us-east-1', stack+'-?')
        print("\nStack: %s" % stack)
        for dns in stack_dns_names:
            try:
                usage_percentage = subprocess.check_output(['ssh', dns, 'df -h | grep \'xvda1\' | awk {\'print $5\'}']).rstrip("\n ")
                percentage_number = int(usage_percentage.rstrip("%\n "))
                print("%s:\t%s" % (dns, usage_percentage))
                if percentage_number > 85:
                    print("\t*** Instance is low on disk space! ***")
                    failure_flag = True
            except:
                print("Could not connect to %s due to an error.  Skipping..." % dns)
    for stack in west1_stacks:
        stack_dns_names = ec2.get_public_dns_by_tag_name(aws_west1_conn, 'us-west-1', stack+'-?')
        print("\nStack: %s" % stack)
        for dns in stack_dns_names:
            try:
                usage_percentage = subprocess.check_output(['ssh', dns, 'df -h | grep \'xvda1\' | awk {\'print $5\'}']).rstrip("\n ")
                percentage_number = int(usage_percentage.rstrip("%\n "))
                print("%s:\t%s" % (dns, usage_percentage))
                if percentage_number > 85:
                    print("\t*** Instance is low on disk space! ***")
                    failure_flag = True
            except:
                print("Could not connect to %s due to an error.  Skipping..." % dns)
    if failure_flag is True:
        print("Marking as FAILURE due to disk space issues.")
        sys.exit(-1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()