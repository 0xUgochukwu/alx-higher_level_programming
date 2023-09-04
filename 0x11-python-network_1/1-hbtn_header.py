#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as res:
        print(res.headers.get('X-Request-Id'))
