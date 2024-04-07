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
        local("mkdir -p versions")

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:

        filename = "versions/web_static_{}.tgz".format(date)
        result = local("sudo tar -cvzf {} web_static".format(filename))

        if result.succeeded:
            return filename
        else:
            return None
    except Exception:
        return None


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
        run("tar -xzf {} -C {}/".format(tmp, name))
        run("rm -r {}".format(tmp))
        run("mv {}/web_static/* {}/".format(name, name))
        run("rm -rf {}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(name))

        return True
    except Exception as e:
        return False


def deploy():
    """Creates and and share the archived file to a web server"""
    try:
        
        file = do_pack()
        if file is None:
            return False
        return do_deploy(file)
    except Exception as e:
        print(e)
        return False