#programming number 5
#MtucX
import requests , re ,os
re = requests.Session()
vars = []
r = re.get("http://.............../Programming/Prog5.php")
r= r.text
solution = ""
list = r.split(' ')
for i in range(len(list)):
	vars.append(int(list[i]))
for i in range(2,len(vars)):
	if(vars[i-1]>= vars[i]):
		if(vars[i-1] >= vars[i-2]):
			solution+=str(vars[i-1])+" "
cookie = str(re.cookies.get_dict())
cookie = cookie.strip("{ }")[14:40]
cm = 'curl --data "azezaeza'+solution[:-1]+'" --cookie "PHPSESSID='+cookie+'"http://....../Programming/Prog5.php'
os.system(cm)