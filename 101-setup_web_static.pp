# configures and prepares web servers for deployment of statusc files


exec { 'install-nginx':
  command     => 'apt-get install -y nginx',
  path        => '/usr/bin',
  unless      => 'dpkg -l nginx',
  user        => 'root',
  logoutput   => true,
  #notify      => Service['nginx'],
}

file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>\n",
}

file { '/data/web_static/current/':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  force  => true,
}

exec { 'chown -R ubuntu:ubuntu /data/':
  command     => 'chown -R ubuntu:ubuntu /data/',
  path        => '/usr/bin',
  refreshonly => true,
}

file { '/var/www/':
  ensure => 'directory',
}

file { '/var/www/html/':
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => "Holberton School Nginx\n",
}

file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page\n",
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
      alias /data/web_static/current;
      index index.html index.htm;
    }

    location /redirect_me {
      return 301 http://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;

    location /404 {
      root /var/www/html;
      internal;
    }
}"
}
