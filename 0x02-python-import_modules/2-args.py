#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]
    length = len(argv)

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(length))
        for i, arg in enumerate(argv):
            print("{}: {}".format(i + 1, arg))

