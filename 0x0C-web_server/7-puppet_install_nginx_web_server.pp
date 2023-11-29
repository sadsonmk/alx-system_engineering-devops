# install nginx package
package { 'nginx':
  ensure  => installed,
}

# configure nginx to listen to port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => <<EOM
server {
  listen 80;

  location / {
    root /usr/share/nginx/html;
    index index.html;
  }
}
EOM
}

file { 'etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => 'etc/nginx/sites-available/default',
}

file { '/usr/share/nginx/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/redirect_me':
  ensure  => present,
  content => <<EOM
server {
  listen 80;

  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4
  }
}
EOM
}

file { '/etc/nginx/sites-enabled/redirect_me':
  ensure  => link,
  target  => '/etc/nginx/sites-available/redirect_me',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}
