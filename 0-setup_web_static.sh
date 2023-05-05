#!/usr/bin/env bash
# Bash script that sets up your web servers
if ! which nginx > /dev/null; then
	apt-get update
	apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
chown -R ubuntu:ubuntu /data/
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
sed -i 's/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/' /etc/nginx/sites-available/default
service nginx restart
