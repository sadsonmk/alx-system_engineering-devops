# Installs a package flask from pip3 using puppet

package { 'flask':
  ensure   => installed,
  provider => 'pip3',
  name     => 'Flask==2.1.0',
}
