#!/usr/bin/python

import requests


def main():
    r = requests.get("http://www.apple.com")
    print(r.status_code)
    print(r.headers)
    print(r.content)


if __name__ == "__main__":
    main()
