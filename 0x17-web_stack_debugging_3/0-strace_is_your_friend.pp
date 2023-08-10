#Puppet script fixes site

$file_url = '/var/www/html/wp-settings.php'
exec { 'fix_site':
  command => "sed -i 's/phpp/php/g' ${file_url}; \
service apache2 restart",
  path    => ['/bin','/usr/bin']
}
