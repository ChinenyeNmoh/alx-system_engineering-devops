# Use Puppet to automate the task of creating a custom HTTP header response

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
file_line { 'add_custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => "\tadd_header X-Served-By ${hostname};",
  after   => 'listen 80 default_server;',
  require => Package['nginx']
}
exec { 'restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
  require => File_line['add_custom_header']
}
