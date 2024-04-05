#!/usr/bin/python3
"""Full deloyment using fabric
"""
from os.path import exists
from datetime import datetime
from fabric.api import *

env.hosts = ['54.237.43.71', '52.87.222.69']


def do_pack():
    """Fabric scripts that generates a .tgz
    """
    if not exists("versions"):
        if local("sudo mkdir -p versions").failed is True:
            return None

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))

    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """Function that deal with the deloyment it self and
    returns false if error is enconted
    """

    if exists(archive_path) is False:
        return False
    filename = archive_path.split("/")[-1]
    try:
        if put(archive_path, "/tmp/").failed is True:
            return False
        archive_filename = path.basename(archive_path)
        release_folder = "/data/web_static/releases/{}".format(
                archive_filename[:-4])
        if run("sudo mkdir -p {}".format(release_folder)).failed is True:
            return False
        if run("sudo tar -xzf /tmp/{} -C {}".format(
                archive_filename, release_folder)).failed is True:
            return False
        if run("sudo rm -rf /tmp/{}".format(archive_filename)).failed is True:
            return False
        if run("sudo rm -rf /data/web_static/current").failed is True:
            return False
        if run("sudo ln -s {} /data/web-static/current".format(
                release_folder)).failed is True:
            return False

        return True
    except Exception:
        return False


def deploy():
    """Creates and and share the archived file to a web server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
