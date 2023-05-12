#!/usr/bin/python3
""" Module use fabric lib to compress a folder to .tgz """

from fabric.api import local
from datetime import datetime

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

        command  = "tar -czvf {} web_static".format(archive_path)
        local(command)

        return archive_path

    except Exception:
        return None
