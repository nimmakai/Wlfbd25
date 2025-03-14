import requests
import welcomeparameters
cat = "+".join(welcomeparameters.Categorytocheck.split())
response = requests.get('https://ptools.toolforge.org/uploadersincat.php?category='+cat)
for uincattxt in response.content.decode("UTF-8").split('fieldset'):
	if '<legend>List</legend>' in uincattxt: break

with open('wlfbd already sent.txt', 'r') as sent:
    asent = sent.read().rstrip()

splt = list(uincattxt.split('>'))
users = "" 

for s in splt:
	if "User:" in s and "href" not in s:
		user = s.replace("User:","").replace("</a","")
		if user not in asent: users+=user+"\n"

with open("wlfbd users to send.txt", "w") as file:
    file.write(users)

print(users)

