#!usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static folder 
# of your AirBnB Clone repo, using the function do_pack.

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Compresses the contents of the web_static folder into a .tgz archive.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        if not os.path.exists('versions'):
            local ('mkdir versions')

        time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"web_static_{time}.tgz"
        local("tar -cvzf versions/{} web_static".format(filename))
        path = 'versions/web_static_{}.tgz'.format(t.strftime(f))

        return path
    except:
        return None
