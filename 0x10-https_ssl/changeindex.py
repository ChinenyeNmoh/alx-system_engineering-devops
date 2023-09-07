#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from fabric.api import env
from fabric.api import sudo


env.hosts = ["34.229.66.208", "100.24.255.208"]
def deploys():
    output = sudo("echo Holberton School > /var/www/html/index.html")
    if output.failed is True:
        print("failed")
    else:
        print("success")
