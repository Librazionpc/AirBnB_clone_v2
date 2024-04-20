#!/usr/bin/python3
"""Clean up outdated archives using fabrics
"""

from fabric.api import *
from os.path import exists

env.hosts = ['54.237.43.71', '52.87.222.69']


def do_clean(number=0):
    """Deletes out-date arrchive based in the number provided
    """
    
    number = int(number)
    if number < 1:
        number = 1
    try:
        with cd("versions"):
            archives = run('ls -tr').split()

            if len(archives) > number:
                to_del = archives[:-number]
                for archive in to_del:
                    run("rm -rf {}".format(archive))
        
        with cd("/data/web_static/releases"):
            archives = run("ls -tr").split()

            if len(archives) > number:
                to_del = archives[:-number]
                for archive in to_del:
                    run("rm -rf {}".format(archive))
    except Exception as e:
        print(e)
        return False