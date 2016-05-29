text = {
	"p":"e",
	"b":"a",
	"x":"i",
	"z":"m",
	"d":"h",
	"a":"n",
	"f":"s",
	"h":"r",
	"s":"y",
	"e":"o",
	"u":"d",
	"n":"g",
	"m":"w",
	"l":"c",
	"j":"l",
	"y":"u",
	"w":"f",
	"g":"v",
	"o":"p",
	"q":"b",
	"i":"k",
	"v":"z",
	"k":"j",
	"c":"q",
	"r":"x",
}

f = open('text.txt', 'r')
content = f.read()
changed = ""

for ch in content:
	if ch.isalpha()!=True:
		changed += ch
		continue
		
	try: 
		tmp = text[ch]
	except:
		tmp = ch
	finally:
		changed += tmp
		
f = open("saved.txt", 'w')
f.write(changed)
f.close()