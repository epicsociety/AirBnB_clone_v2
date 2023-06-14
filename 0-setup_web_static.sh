#!/usr/bin/env bash
<<<<<<< HEAD
# Bash script that sets up the web servers
if ! which nginx > /dev/null; then
	apt-get -y  update
	apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

sed -i 's|^.*server_name.*$|    server_name _;\n    location /hbnb_static {\n        alias /data/web_static/current/;\n    }|' /etc/nginx/sites-available/default
service nginx restart

exit 0
=======
# Bash script that sets up your web servers
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/web_static
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i 's/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/' /etc/nginx/sites-available/default
sudo service nginx restart
>>>>>>> 8a78055778f16e45f18eea9b2189f2dd9ea5c608
