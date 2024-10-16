#!/usr/bin/python3

import os

def del_user():
    confirm = "N"
    while confirm == "Y":
        username = input("Enter the name of the user you want to delete: ")
        print("Delete the username '" + username + "'? (Y/N)")
        confirm = input().upper()

    os.system("sudo userdel -r" + username)

del_user()