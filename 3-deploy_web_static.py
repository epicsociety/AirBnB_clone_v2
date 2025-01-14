#!/usr/bin/python3
<<<<<<< HEAD
""" Module use fabric lib to compress a folder to .tgz
distributes the archive to the webservers
"""

import os
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import runs_once
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ["100.26.236.5", "100.25.144.135"]


@runs_once
def do_pack():
    """ Generate a .tgz archive from the contents of the given webstatic folder
    Returns:
        path to the archive
    """
    try:
        local("mkdir -p versions;", capture=True)
        # generate the archive path using 2023-05-11 23:46
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        command = "tar -czvf {} web_static".format(archive_path)
        local(command)

        return archive_path

    except Exception:
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
>>>>>>> 8a78055778f16e45f18eea9b2189f2dd9ea5c608
        return None


def do_deploy(archive_path):
<<<<<<< HEAD
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


def deploy():
    """ Call the functions that create and distribute the archive"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
=======
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
        return False
    return True

def deploy():
    """
        Interface for set-up functions
    """
    path = do_pack()
    if path is None:
        return False
    else:
        value = do_deploy(path)
        return value
>>>>>>> 8a78055778f16e45f18eea9b2189f2dd9ea5c608
