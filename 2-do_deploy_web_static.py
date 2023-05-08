#!/usr/bin/python3

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
        return False
    return True
