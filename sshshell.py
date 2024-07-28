#!/usr/bin/env python3
import paramiko # type: ignore
from getpass import getpass




host = input("Enter your Host: ")
username = input("Enter your Username: ")
password = getpass("Enter your Password: ")

# Create an SSH client
clt = paramiko.SSHClient()
clt.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Corrected line

# Connect to the host
clt.connect(host, username=username, password=password)

# Receive a command from the client
command = input("=> ")
stdin, stdout, stderr = clt.exec_command(command)
print(stdout.read().decode())


