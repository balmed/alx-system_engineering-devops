# execute pkill command to kill bashscript file killmenow
exec { 'pkill killmenow':
        path => '/usr/bin:/usr/sbin:/bin'
}
