#Mtucx
string = "zaeazeazezaeaz"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0,-20,-1):
	key = ""
	for ch in string:
		if ch == " ":
			key += " "
		elif ch in lower:
			key += lower[lower.find(ch)+i]
		elif ch in upper:
			key += upper[upper.find(ch)+i]
	print str(i),"=>",key
