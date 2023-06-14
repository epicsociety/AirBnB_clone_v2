#!/usr/bin/python3
<<<<<<< HEAD
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
=======

import os
import tarfile
import datetime
from fabric.api import *
from fabric.operations import run, put
from os import path

env.hosts = ['54.157.174.94', '100.25.22.146']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive"""
    
    try:            
        if not path.exists("versions"):
            local("mkdir versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "web_static_" + now
        local("tar -cvzf versions/{}.tgz web_static/".format(name))
        size_of_file = path.getsize("./versions/{}.tgz".format(name))
        print("web_static packed: versions/" + name + ".tgz -> " + size_of_file + " Bytes")
    except BaseException:
        return None


def do_deploy(archive_path):
    '''
         Deploys an archive to the web servers
    '''
    filename = os.path.basename(archive_path)
    if not os.path.exists(archive_path):
         return False

    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    run("mkdir -p /data/web_static/releases/{}".format(filename[:-4]))
    cmd = "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(filename, filename[:-4])
    result = run(cmd)
    if result.failed:
        return False
    result = run("rm /tmp/{}".format(filename))
    if result.failed:
        return False
    run("cp -rp /data/web_static/releases/{}/web_static/*\
                    /data/web_static/releases/{}/".format(filename[:-4], filename[:-4]))
    run("rm -rf /data/web_static/releases/{}/web_static/".format(filename[:-4]))
    result = run("rm /data/web_static/current")
    if result.failed:
        return False
    path = "/data/web_static/releases/{}".format(filename[:-4])
    cmd = "ln -sf {} /data/web_static/current".format(path)
    result = run(cmd)
    if result.failed:
>>>>>>> 8a78055778f16e45f18eea9b2189f2dd9ea5c608
        return False
    return True
