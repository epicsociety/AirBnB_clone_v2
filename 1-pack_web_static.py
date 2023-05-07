#!/usr/bin/python3
"""
    A script that will create compress file from files in web_static folder
"""

from fabric.api import local
from os import path
import tarfile
from datetime import datetime

def do_pack():
    """
        Generates a compress file from web_static folder
    """
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
