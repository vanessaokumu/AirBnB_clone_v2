#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

#Check if nginx is installed
apt-get update
apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
<<<<<<< HEAD
echo "Welcome to this page" > /data/web_static/releases/test/index.html
=======
echo "Welcome to your_domain" > /data/web_static/releases/test/index.html
>>>>>>> 08a43a5e4100848f32cf514b99f33ddcadac6b61
ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu:ubuntu /data/

<<<<<<< HEAD
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service start nginx
=======
ADD_WEBSTATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "35i $ADD_WEBSTATIC" /etc/nginx/sites-available/default

sudo service start nginx
>>>>>>> 08a43a5e4100848f32cf514b99f33ddcadac6b61
