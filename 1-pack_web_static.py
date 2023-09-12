# Fabric script that generates a .tgz archive from the contents of the web_static folder 
# of your AirBnB Clone repo, using the function do_pack.

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    
    try:
        if not os.path.exists('versions'):
            os.mkdir('versions')

        time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"web_static_{time}.tgz"

        local("tar -cvzf versions/{} web_static".format(filename))

        return path
    except:
        return None
