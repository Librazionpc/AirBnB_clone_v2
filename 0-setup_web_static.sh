#!/usr/bin/env bash
#Seetting up my server

sudo apt-get update

if ! dpkg -s nginx >/dev/null 2>&1; then
        sudo apt-get install -y nginx
fi

sudo mkdir -p /data/
sudo chown -R "ubuntu":"ubuntu" /data/
sudo chmod  -R 777 /data/

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p //data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config
sudo service nginx restart
