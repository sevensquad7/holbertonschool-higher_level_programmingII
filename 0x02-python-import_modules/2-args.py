#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    l = len(sys.argv) - 1
    
    print("{:d} {}{}".format(l , "arguments" if l <= 0 else "argument",
                                 ":" if l == 1 else "."))
    for i in range(1, l + 1):
        print("{:d}: {}".format(i, l[i]))
