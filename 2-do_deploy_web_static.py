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
    try:
        put(archive_path, "/tmp/")
        archive_filename = path.basename(archive_path)
        release_folder = "/data/web_static/releases/{}".format(
                archive_filename[:-4])
        run("sudo mkdir -p {}".format(release_folder))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_filename,
            release_folder))
        run("sudo rm -rf /tmp/{}".format(archive_filename))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(release_folder))

        return True
    except Exception:
        return False
