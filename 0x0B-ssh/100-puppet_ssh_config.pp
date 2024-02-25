# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

file_line { 'etc/ssh/ssh-config':
  ensure=>present,

  content=>"
	#SSH Client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	',
}
