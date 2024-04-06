#!/usr/bin/python3
"""Deloyment Using fabric
"""

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.237.43.71', '52.87.222.69']


def do_deploy(archive_path):
    """Function that deal with the deloyment it self and
    returns false if error is enconted
    """

    if exists(archive_path) is False:
        return False
    filename = archive_path.split("/")[-1]
    name = '/data/web_static/releases/' + "{}".format(filename.split(".")[0])
    tmp = '/tmp/' + filename
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}/".format(name))
        print(name)
        run("tar -xzf {} -C {}/".format(tmp, name))
        run("rm -r {}".format(tmp))
        run("mv {}/web_static/* {}/".format(name, name))
        run("rm -rf {}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(name))

        return True
    except Exception as e:
        return False
