#!/usr/bin/env bash
# Bash script that sets up the web servers
if ! which nginx > /dev/null; then
	apt-get -y  update
	apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

chown -R ubuntu:ubuntu /data

echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
sed -i 's|^.*server_name.*$|    server_name _;\n    location /hbnb_static {\n        alias /data/web_static/current/;\n    }|' /etc/nginx/sites-available/default
service nginx restart

exit 0
