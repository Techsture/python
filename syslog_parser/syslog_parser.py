#!/usr/bin/env python

# Small script to search through syslog files.
# Assumes there's a syslog file in the script directory (./)


def main():
    syslog = open("syslog", "r")
    program_counter = {}
    for line in syslog:
        split_line = line.split()
        program_name = split_line[4]
        if program_name not in program_counter:
            program_counter[program_name] = 1
            print(program_counter)
        else:
            program_counter[program_name] += 1
            print(program_counter)


if __name__ == '__main__':
    main()
