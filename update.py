import os

def update_environment():
    os.system("sudo yum update")
    os.system("sudo yum upgrade")
    os.system("sudo yum dist-upgrade")
