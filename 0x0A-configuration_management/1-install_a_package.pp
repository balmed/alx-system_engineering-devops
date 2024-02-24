# Install package flask
package { 'flask':
  ensure    =>  'version',
  provider  =>  'pip3', 
}
