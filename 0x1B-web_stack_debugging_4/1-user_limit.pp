# Change the Operinting Systeme configuration so that it is possible to login with the
# holberton user and open a file without any error message
# fix the limit server nginx.

exec { 'myfix':
command => 'sed -i "/ULIMIT=/c\ULIMIT=\"-n 2000\"" /etc/default/nginx',
path    => '/bin',
}
service { 'nginx':
ensure    => running,
subscribe => Exec['myfix'],
}
