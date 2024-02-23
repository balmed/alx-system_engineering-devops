# execute pkill command to kill bashscript file killmenow
exec { 'pkill':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin']
}
