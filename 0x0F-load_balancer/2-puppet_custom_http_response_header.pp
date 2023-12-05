#  automates the task of creating a custom HTTP header response
exec { 'command':
  command => apt-get update;
  apt-get -y install nginx;
  sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default  
  service nginx restart,
  provider => shell,
}
