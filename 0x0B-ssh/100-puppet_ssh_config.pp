#!/usr/bin/env bash
# client configuration with puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
}

file_line { 'configure private key':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentityFile',
}

file_line { 'Ignore password':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#PasswordAuthentication',
}

