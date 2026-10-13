#!/usr/bin/env python3
# Stretch Yourself - Prime numbers
#By Arsyad Ali Mahardika

def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is NOT prime")
