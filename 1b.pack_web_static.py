#!/usr/bin/python3
import tarfile
from os import path
import time
from fabric.api import local

def do_pack():
    try:
        time = time().strftime("%Y%m%d%H%M%S")
        name = "web_static_{}".format(time)
        if not path.exists("versions"):
            local("mkdir versions")
        local()
