#!/usr/bin/env python3
# Sample script that reads from a file
#By Arsyad Ali Mahardika

print("Here is someone to hack - information")
with open("hackme.txt", "r") as f:
    for line in f:
        print(line.strip())
