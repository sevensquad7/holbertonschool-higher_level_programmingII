#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    lenarg = len(sys.argv) - 1
    text = "arguments"
    sig = ":"
    argv = sys.argv

    if lenarg == 0:
        sig = "."

    if lenarg == 1:
        text = "argument"

    print("{:d} {}{}".format(lenarg, text, sig))

    for i in range(1, lenarg + 1):
        print("{:d}: {}".format(i, argv[i]))
