#!/usr/bin/env bash
#set up a web server

source_dir="/data/web_static/releases/test/"
symbolic_link="/data/web_static/current"
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
if [ -L "$symbolic_link" ];
then
        rm -d "$symbolic_link"
fi
sudo ln -s "$source_dir" "$symbolic_link"
sudo chown -R "ubuntu":"ubuntu" /data/

sudo sed -i "48i \\\tlocation /hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t\}" /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx restart
