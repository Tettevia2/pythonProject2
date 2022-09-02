# Password Manager
import random
import string
import hashlib
import binascii
import os

# print(string.ascii_letters)
import basehash as basehash

print()


def store_password():
    # username
    username = str(input("Your username:  "))
    # website
    website = str(input("Website:  "))
    # generate random password
    digit = int(input("How many digit do you want? (integer only) "))
    password = ""
    for i in range(digit):
        char = random.choice(string.ascii_letters)
        password += char

    basehash.base36().encode(password)

    # store the password into a file
    f = open("password_manager.text", "a")
    f.write(f"{username}-{website}-{password}")
    f.close()


def search():
    username_or_website = str(input("Do you want to search for username or website? "))
    value = str(input("What value? "))
    f = open("password_manager.text", "r")
    for line in f:
        if username_or_website == "username":
            line.split("-")

            # search by username
        else:
            # search by website

            pass


store_password()
