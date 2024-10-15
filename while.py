#!/usr/bin/python3
name = input("Enter your name: ")

while name == "":
    print(" You did not enter your name")
    name = input("Enter your name: ")

print(f"Hell {name}")

