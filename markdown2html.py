#!/usr/bin/python3
'''Start a script'''
from sys import argv, stderr


if __name__ == "__main__":
    if (len(argv) < 3):
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    else:
        try:
            with open(argv[1], encoding="utf-8") as markdown:
                exit
        except:
            print("Missing {}".format(argv[1]), file=stderr)
            exit(1)
