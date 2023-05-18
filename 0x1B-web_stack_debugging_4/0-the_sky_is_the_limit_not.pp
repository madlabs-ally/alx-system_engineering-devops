exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin',
  notify  => Exec['nginx-restart'],  # Notify the restart when this exec is applied
}

exec { 'nginx-restart':
  command     => 'service nginx restart',
  refreshonly => true,  # Only execute if notified by another resource
}
