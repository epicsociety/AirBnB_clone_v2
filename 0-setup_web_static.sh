#!/usr/bin/env bash
# Bash script that sets up your web servers
if ! which nginx > /dev/null; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i 's/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/' /etc/nginx/sites-available/default
sudo service nginx restart