#!/usr/local/bin/python

# Write a script which parses "var/log/messages" and generates a CSV with two columns: minute, number_of_messages in sorted time order.
# ---------- begin sample output ----------
# minute, number_of_messages
# Jan 20 03:25,2
# Jan 20 03:26,2
# Jan 20 03:30,2
# Jan 20 05:03,1
# Jan 20 05:20,1
# Jan 20 05:22,6
# ---------- end sample output ------------

def main():
    filename = open('var/log/messages', 'r')
    minute_counter = {}
    for line in filename.readlines():
        message = line.split()
        month = message[0]
        day = message[1]
        time = message[2].split(':')
        time_stamp = month + ' ' + day + ' ' + time[0] + ':' + time[1]
        if time_stamp not in minute_counter:
            minute_counter[time_stamp] = 1
        else:
            minute_counter[time_stamp] += 1
    print("minute, number_of_messages")
    for time in sorted(minute_counter.keys()):
        print("%s,%s" % (time, minute_counter[time]))

if __name__ == '__main__':
    main()