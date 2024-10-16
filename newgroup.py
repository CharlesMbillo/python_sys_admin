#!/usr/bin/python3

import os

def add_group():
    confirm = "N"
    while confirm != "Y":
        groupname = input("Enter the name of the group: ")
        print("Create the group '" + groupname + "'? (Y/N)")
        confirm = input().upper()

    os.system("sudo groupadd " + groupname)

add_group() 
