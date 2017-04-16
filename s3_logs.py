#!/usr/bin/python

# This script will look for logrotated *.gz files in /logs/.  If it finds any, it will S3PUT the files and then delete them afterwards.

import os
from subprocess import call


def main():
  contents = os.walk("/logs")
  for directory, subdirectory, file_list in os.walk('/logs'):
    for filename in file_list:
      if '.gz' in filename:
        # Skip any files that contain "%{" since these are parsing errors that we don't have to back up.
        if '%{' in filename:
          continue
        else:
          full_filename = directory + "/" + filename
          # Copy the file to S3
          cmd = ['s3put', '-b', 'BUCKET_NAME', '--region', 'REGION', '-p', '/logs/', full_filename]
          call(cmd)
          # Delete the file after it's been copied
          cmd = ['rm', '-rf', full_filename]
          call(cmd)
          
if __name__ == "__main__":
  main()
