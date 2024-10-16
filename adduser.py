import os
import subprocess

def add_user(username, password):
    try:
        # Check if the user already exists
        user_check = subprocess.run(['id', '-u', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if user_check.returncode == 0:
            print(f"User {username} already exists.")
            return
        
        # Add the user
        subprocess.run(['sudo', 'useradd', '-m', '-s', '/bin/bash', username])
        # Set the user's password
        subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{password}".encode())
        print(f"User {username} has been added successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage

username = input("Enter username to add: ")
password = "password123"
add_user(username, password)
