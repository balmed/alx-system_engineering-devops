# Install package flask
package { 'Flask':
  ensure   => 'version',
  provider => pip3,
}
