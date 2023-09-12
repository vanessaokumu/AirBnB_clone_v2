#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

#Check if nginx is installed
apt-get update
apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "Welcome to this page" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu:ubuntu /data/

sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service start nginx
exit 0
