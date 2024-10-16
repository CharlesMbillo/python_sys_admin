#!/usr/bin/python3

import subprocess

def list_groups():
    """List all groups on the system."""
    try:
        # Get the list of groups from the system
        result = subprocess.run(['getent', 'group'], stdout=subprocess.PIPE, text=True)
        if result.returncode == 0:
            groups = [line.split(":")[0] for line in result.stdout.splitlines()]
            return groups
        else:
            print("Error retrieving groups")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def add_user_to_group(username, group):
    """Add the specified user to the given group."""
    try:
        result = subprocess.run(['sudo', 'usermod', '-aG', group, username], stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"User '{username}' successfully added to group '{group}'.")
        else:
            print(f"Failed to add user '{username}' to group '{group}': {result.stderr.decode().strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Get the username
    username = input("Enter the username to add to a group: ")

    # List available groups
    available_groups = list_groups()
    if not available_groups:
        print("No groups available.")
        return

    print("\nAvailable groups:")
    print(" ".join(available_groups))

    # Get the group names from the user
    group_names = input("\nEnter the group names (separated by space) to add the user to: ").split()

    # Add user to each specified group
    for group in group_names:
        if group in available_groups:
            add_user_to_group(username, group)
        else:
            print(f"Group '{group}' does not exist.")

if __name__ == "__main__":
    main()
