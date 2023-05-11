from fabric.api import local
from datetime import datetime

def do_pack():
    """ Generate a .tgz archibe from the contents of the given webstatic folder"""
    # Create the version folder
    local("mkdir -p versions")

    # generate the archive path using 2023-05-11 23:46
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    command  = "tar -czvf {} web_static".format(archive_path)
    result = local(command, capture=True)

    if result.succeeded:
        return archive_path
    else:
        return None
