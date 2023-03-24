# A manifest that executes a bash command
# bash commnad kills a process
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
