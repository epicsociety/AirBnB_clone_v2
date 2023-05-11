#!/usr/bin/python3

from fabric.api import *

#env.user = 'ubuntu'
#env.hosts = ['ubuntu@100.26.236.5']

def host_type():
    run('uname -s')
