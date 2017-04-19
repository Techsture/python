#!/usr/local/bin/python

# Write a script which parses "var/log/messages" and generates a CSV with n columns: minute, number_of_messages, 
#   and name of all processes in sorted time order.
# 
# Extract the program name from the field between the hostname and the log message and output those values in columns.
# ---------- begin sample output ----------
# minute,total_count,logrotate,run-parts,anacron,CROND,ntpd,rsyslogd,cs3,ACCT_ADD
# Jan 20 03:25,2,1,1,0,0,0,0,0,0
# Jan 20 03:26,2,0,0,2,0,0,0,0,0
# Jan 20 03:30,2,0,0,0,2,0,0,0,0
# Jan 20 05:03,1,0,0,0,0,1,0,0,0
# Jan 20 05:20,1,0,0,0,0,0,1,0,0
# Jan 20 05:22,6,0,0,0,0,0,0,5,1
# ---------- end sample output ------------
# Note: It is important that your program work with any arbitrary set of programs, not just the ones in the example output.

import re

def main():
    filename = open('var/log/messages', 'r')
    minute_counter = {}
    prog_counter = {}
    pid_pattern = re.compile(r"\:|\[\d*\]\:|\(.*\)")
    for line in filename.readlines():
        message = line.split()
        month = message[0]
        day = message[1]
        time = message[2].split(':')
        time_stamp = month + ' ' + day + ' ' + time[0] + ':' + time[1]
        prog_name = re.sub(pid_pattern, '', message[4])
        if time_stamp not in minute_counter:
            minute_counter[time_stamp] = 1
            if prog_name not in prog_counter:
                prog_counter[prog_name] = 1
            else:
                prog_counter[prog_name] += 1
        else:
            minute_counter[time_stamp] += 1
            if prog_name not in prog_counter:
                prog_counter[prog_name] = 1
            else:
                prog_counter[prog_name] += 1
    header_string = "minute,number_of_messages,"
    for prog_name in sorted(prog_counter.keys()):
        header_string += prog_name + ','
    print(header_string.rstrip(','))
    print(minute_counter)
    print(prog_counter)
    for time in sorted(minute_counter.keys()):
        output_string = time + ","  + str(minute_counter[time]) + ","
        for prog_name in sorted(prog_counter.keys()):
            output_string += str(prog_counter[prog_name]) + ','
        print(output_string.rstrip(','))


if __name__ == "__main__":
    main()
