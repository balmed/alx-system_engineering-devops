# fix the limit server nginx.
exec { 'fix--for-nginx':
command => 'sed -i "/ULIMIT=/c\ULIMIT=\"-n 2000\"" /etc/default/nginx',
path    => '/bin',
}
service { 'nginx':
ensure    => running,
subscribe => Exec['fix--for-nginx'],
}
