#!/usr/bin/env python3
# Sample script that writes to a file
#By Arsyad Ali Mahardika

name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
maiden = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

with open("hackme.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Favorite color: {color}\n")
    f.write(f"First pet: {pet}\n")
    f.write(f"Mother's maiden name: {maiden}\n")
    f.write(f"Elementary school: {school}\n")

print("Saved to hackme.txt")
