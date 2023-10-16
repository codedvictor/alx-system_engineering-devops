# testing Nginx under pressure
# using ApacheBench

# Ensure Nginx is up to date
package { 'nginx':
  ensure  => 'latest',
}

# Increase the limit
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin'],
  onlyif  => 'grep -q "15" /etc/default/nginx',  # Make sure the value 15 is present
}

# Set the ulimit variable
file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 4096"',
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Exec['increase_nginx_limit'], File['/etc/default/nginx']],  # Ensure the limit change happens first
}
