#!/usr/bin/python3
""" Modules deletes previous archives"""


from fabric.api import local, env, run, lcd


env.user = 'ubuntu'
env.hosts = ["100.26.236.5", "100.25.144.135"]


def do_clean(number=0):
    """ deletes older archives
    Args:
        number(int): number of available archives
    """

    number = int(number)
    if number <= 0:
        number = 1
    else:
        number

    with lcd("versions"):
        archives = sorted(local("ls -1tr", capture=True).split())
        archives_to_delete = archives[:-number]
        [local("rm -f {}".format(archive)) for archive in archives_to_delete]

    with cd("/data/web_static/releases"):
        archives = sorted(run("ls -1tr | grep 'web_static_ '").split())
        archives_to_delete = archives[:-number]
        [run("rm -rf {}".format(archive)) for archive in archives_to_delete]
