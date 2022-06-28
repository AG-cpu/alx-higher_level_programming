#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digt = abs(number) % 10
if number < 0:
    digt = -digt
print("Last digit of {} is {} and is ".format(number, digt), end="")
if digt > 5:
    print("greater than 5")
elif digt == 0:
    print("0")
else:
    print("less than 6 and not 0")
