#!/usr/bin/env python

import argparse
import socket

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("address", help="address to test", type=str)
    parser.add_argument("port", help="port to test", type=int)
    args = parser.parse_args()
    proc_socket = socket.socket()
    try: 
        proc_socket.connect((args.address, args.port))
        print("OPEN")
    except:
        print("CLOSED")
    proc_socket.close()

if __name__ == "__main__":
    main()