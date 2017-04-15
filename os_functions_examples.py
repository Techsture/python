#!/usr/local/bin/python
# This demonstrates some of the os module functions that might be useful for sysadmin tasks.

# All the functions used in this script are part of the 'os' module, so you need to import it:
import os


def main():
    # Run a command:
    print("### os.system() ###")
    os.system('ls -lahrt')
    print("\n")

    # Get the status of a file:
    print("### os.stat() ###")
    filename = 'os_functions_examples.py'
    file_stat = os.stat(filename)
    print("Filename:\t\t%s" % filename)
    print("Raw os.stat() output:\n %s" % file_stat)
    print("File mode:\t\t%s" % file_stat[0])
    print("File inode:\t\t%s" % file_stat[1])
    print("Device:\t\t\t%s" % file_stat[2])
    print("Number of links:\t%s" % file_stat[3])
    print("File owner user ID:\t%s" % file_stat[4])
    print("File owner group ID:\t%s" % file_stat[5])
    print("File size:\t\t%s" % file_stat[6])
    print("File accessed time:\t%s" % file_stat[7])
    print("File modified time:\t%s" % file_stat[8])
    print("File changed time:\t%s" % file_stat[9])
    print("\n")

    # Get environment variable details:
    print("### os.environ() ###")
    print("HOME:\t%s" % os.environ['HOME'])
    print("PATH:\t%s" % os.environ['PATH'])
    print("SHELL:\t%s" % os.environ['SHELL'])
    print("TMPDIR:\t%s" % os.environ['TMPDIR'])
    print("USER:\t%s" % os.environ['USER'])
    print("\n")

    # Get and change current working directory:
    print("### os.chdir() & os.getcwd() ###")
    previous_directory = os.getcwd()
    print("Current directory:\t%s" % os.getcwd())
    print("Running command: os.chdir('/tmp')")
    os.chdir('/tmp')
    print("Current directory:\t%s" % os.getcwd())
    print("Changing back to previous directory...")
    os.chdir(previous_directory)
    print("Current directory:\t%s" % os.getcwd())
    print("\n")
    
    # Get information about the current process:
    print("### os.getgid() & os.getuid() & os.getpid() ###")
    print("Group ID:\t%s" % os.getgid())
    print("User ID:\t%s" % os.getuid())
    print("Process ID:\t%s" % os.getpid())
    print("\n")

    # Get currently logged in user:
    print("### os.getlogin() ###")
    print("Current user:\t%s" % os.getlogin())
    print("\n")

    # Check file accessibility:
    print("### os.access() ###")
    print("Does %s exist?\t%s" % (filename, os.access(filename, os.F_OK)))
    print("Is %s readable?\t%s" % (filename, os.access(filename,os.R_OK)))
    print("Is %s writable?\t%s" % (filename, os.access(filename,os.W_OK)))
    print("Is %s executable?\t%s" % (filename, os.access(filename,os.X_OK)))
    print("\n")

    # Check if a file exists and its size:
    print("### os.path.exists() & os.path.getsize() ###")
    print("Does %s exist?\t\t%s" % (filename, os.path.exists(filename)))
    print("What is the size of %s?\t%s" % (filename, os.path.getsize(filename)))
    print("\n")

    # Get the current directory and all its subdirectories and files:
    print("### os.walk() ###")
    for root, dirs, files in os.walk(os.getcwd()):
        print("ROOT:\t\t%s" % root)
        print("DIRECTORIES:\t%s" % dirs)
        print("FILES:\t\t%s" % files)
    print("\n")

    # Get system information:
    print("### os.uname() ###")
    sys_info = os.uname()
    print("OS Name:\t%s" % sys_info[0])
    print("Node Name:\t%s" % sys_info[1])
    print("Release:\t%s" % sys_info[2])
    print("Version:\t%s" % sys_info[3])
    print("Architecture:\t%s" % sys_info[4])
    print("\n")

    # Get system load average:
    print("### os.getloadavg() ###")
    load_average = os.getloadavg()
    print("1m Load:\t%s" % load_average[0])
    print("5m Load:\t%s" % load_average[1])
    print("15m Load:\t%s" % load_average[2])
    print("\n")

    # Get all files and directories in a path:
    print("### os.listdir() ###")
    print("Files In Current Directory:\t%s" % os.listdir('.'))
    print("Files In Root Directory:\t%s" % os.listdir('/'))
    print("\n")


if __name__ == "__main__":
    main()