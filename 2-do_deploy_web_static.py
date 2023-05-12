#!/usr/bin/python3
""" Module put the archive to webservers"""

from fabric.api import env, put, run
import os


env.user = 'ubuntu'
env.hosts = ["100.26.236.5", "100.25.144.135"]


def do_deploy(archive_path):
    """ distributes an archive to your web servers
    Args:
        archive_path(str): path to the archive to distribute
    Returns:
        True if successful and false if not or the archive does not exist
    """
    if not os.path.exists(archive_path):
        return False
    archive_name = archive_path.split("/")[-1]
    file_name = archive_name.split(".")[0]

    if put(archive_path, "/tmp/{}".format(archive_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(file_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(file_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(archive_name, file_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(archive_name)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* \
           /data/web_static/releases/{}/".
           format(file_name, file_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_name)).failed is True:
        return False
    return True
