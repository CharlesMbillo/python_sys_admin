#!/usr/bin/python3

import os

def update_environment():
    os.system("sudo yum update")
    os.system("sudo yum upgrade")
    # os.system("sudo apt-get dist-upgrade")

update_environment()