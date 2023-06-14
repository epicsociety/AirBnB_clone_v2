#!/usr/bin/python3
<<<<<<< HEAD
""" Module use fabric lib to compress a folder to .tgz """

from fabric.api import local
=======
"""
    A script that will create compress file from files in web_static folder
"""


from fabric.api import local
from os import path
import tarfile
>>>>>>> 8a78055778f16e45f18eea9b2189f2dd9ea5c608
from datetime import datetime


def do_pack():
<<<<<<< HEAD
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
        print("web_static packed: versions/{}.tgz -> {} Bytes".format(name, size_of_file))
    except BaseException:
>>>>>>> 8a78055778f16e45f18eea9b2189f2dd9ea5c608
        return None
