#!/usr/bin/env python3
# example workign with Functions
#By Arsyad Ali Mahardika

def send_message():
    for x in range(10):
        print("Yeah it is")

answer = input("Is today a good day? (y/n) ")
if answer == "y":
    send_message()
