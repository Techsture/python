#!/usr/local/bin/python

# This script demonstrates the subprocess module, so that needs to be imported:
import subprocess

def main():
    # Issue a system command
    print("### subprocess.call() ###")
    subprocess.call(['ls', '-lahrt'])
    print("\n")

    # Issue a system command and allow the output to be written to a variable
    print("### subprocess.check_output() ###")
    output = subprocess.check_output(['ls', '-lahrt'])
    print(output)
    print("\n")

    # Example of working with system output using subprocess
    # This will print all *.py files in the current directory
    print("### Find all *.py files in the current directory ###")
    # First, get the output
    output = subprocess.check_output(['ls', '-lahrt'])
    # Split the output on any whitespace (spaces, tabs, newline, etc)
    output_rows = output.split()
    # For each item in the split output, see if it contains the substring '.py'.
    # If it does, print the filename out.
    for item in output_rows:
        if '.py' in item:
            print("Found a python file:\t%s" % item)


if __name__ == "__main__":
    main()
