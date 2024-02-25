# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

include stdlibe

file { 'etc/ssh/ssh-config':
  ensure=>present,

  content=>"
    #SSH Client configuration
    host*
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    ^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$
    ^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$
    ",
}
