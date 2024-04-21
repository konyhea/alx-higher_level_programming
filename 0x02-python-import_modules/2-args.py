#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len = len(sys.argv) - 1
    if len == 0:
        print(f"{len} arguments.", end="\n")
    elif len == 1:
        print(f"{len} argument:", end="\n")
        print(f"{len}: {sys.argv[1]}")
    else:
        print(f"{len} arguments:")
        for i in range(1, len + 1):
            print(f"{i}: {sys.argv[i]}")
