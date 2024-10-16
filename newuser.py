import os
import subprocess

def add_user():
    confirm = "N"
    while confirm == "Y":
        username = input("Enter the name of the user: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()

    os.system("sudo adduser " + username)

add_user() 

        

# Example usage
username = "newuser"
password = "password123"
add_user(username, password)
