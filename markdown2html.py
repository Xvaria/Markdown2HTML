#!/usr/bin/python3
'''Start a script'''
from sys import argv


if __name__ == "__main__":
    if (len(argv) < 2):
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    else:
        try:
            with open(argv[1], encoding="utf-8") as markdown:
                text = markdown.read()
            with open(argv[2], mode="w", encoding="utf-8") as HTMLfile:
                print
                HTMLfile.write(text)
                exit
        except:
            print("Missing {}".format(argv[1]))
            exit(1)
