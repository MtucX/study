a = "gur synt vf zghpk"

for i in range(0,26):
	print "==== test %d" % i
	dec = ""
	for c in a:
		if ord(c)>=ord('a') and ord(c)<=ord('z'):
			dec += chr((((ord(c)+ord('a'))+i)%26)+ord('a'))
		elif ord(c)>=ord('A') and ord(c)<=ord('Z'):
			dec += chr((((ord(c)+ord('A'))+i)%26)+ord('A'))
		else:
			dec += c
	print dec