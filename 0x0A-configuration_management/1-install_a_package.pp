#!/usr/bin/pup
# Install package flask

package { 'flask':
  ensure    =>  '2.1.0',
  provider  =>  'pip3', 
}
notify { 'Flask installed':
  message => 'Flask package installation completed.',
}

package { 'Werkzeug':
  ensure    =>  '2.1.1',
  provider  =>  'pip3', 
}
notify { 'Werkzeug installed':
  message => 'Werkzeug package installation completed.',
}
