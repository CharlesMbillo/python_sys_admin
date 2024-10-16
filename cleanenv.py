import os

def clean_environment():
    os.system("sudo yum autoremove")
    # os.system("sudo apt-get autoclean")

clean_environment()