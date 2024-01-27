# changing the user limit

# hard limt change
exec { 'increase-the-hard-limit':
  command => "sed -i '/^holberton hard/s/5/30000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# soft limit change
exec { 'increase-the-soft-limit':
  command => "sed -i '/^holberton soft/s/4/30000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
