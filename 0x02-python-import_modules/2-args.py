#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    l = len(sys.argv) - 1
    text = "arguments"
    sig = ":"
    argv = sys.argv

    if l == 0:
        sig = "."

    if l == 1:
        text = "argument"

    print("{:d} {}{}".format(l, text, sig))

    for i in range(1, l + 1):
        print("{:d}: {}".format(i, argv[i]))
