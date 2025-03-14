codedoc = """
todo
"""

import os               # Operating system: getenv
import sys		    	# System: argv, exit (get the parameters, terminate the program)
import pywikibot
from datetime import datetime	# now, strftime, delta time, total_seconds
import welcomeparameters		# imports all the parameters

messagetitle = welcomeparameters.editsummery
mailtitle = welcomeparameters.mailsubject
usermessage = welcomeparameters.talkpagemessage
mailmessage = welcomeparameters.mailmessage

# Get program parameters
pgmnm = sys.argv.pop(0)
mainlang = os.getenv('LANG', 'commons')[:2]     # Default description language
wmproject = 'commons'

if len(sys.argv) > 0:
    mainlang = sys.argv.pop(0)

if len(sys.argv) > 0:
    wmproject = sys.argv.pop(0)

# Login to the Wikimedia account
site = pywikibot.Site(wmproject)
site.login()    # Must login to get the logged in username
account = pywikibot.User(site, site.user())

try:    # Old accounts do not have a registration date
    accregdt = account.registration().strftime('%Y-%m-%d')
except Exception:
    accregdt = ''

print('Account:', site.user(), account.editCount(), accregdt, account.groups(), file=sys.stderr)
print(site, file=sys.stderr)

skipcnt = 0
usercnt = 0
usermel = 0
usererr = 0

with open('wlfbd users to send.txt', 'r') as file:
    inputfile = file.read().rstrip()
#inputfile = sys.stdin.read()
#inputfile = "Kaim Amin"
alsent = ""
itemlist = sorted(set(inputfile.split('\n')))

for user in itemlist:
  if user > '/':
    try:
        wikiuser = pywikibot.User(site, user)
        wp = wikiuser.getprops()
        if 'userid' not in wp:
            print('User %s does not exist' % (user), file=sys.stderr);skipcnt += 1
        elif wikiuser.isEmailable():
        	wikiuser.send_email(mailtitle,mailmessage,ccme=True)
        	print("Mailed User:"+user)
        	alsent+=user+"\n"
        	usermel += 1
        else:
            page = pywikibot.Page(site,'User_talk:' + user)
            page.text += usermessage
            page.save(messagetitle)
            alsent+=user+"\n"
            usercnt += 1
    
    except Exception as error:
        print(format(error), file=sys.stderr)
        usererr += 1

with open("wlfbd already sent.txt", "r") as file:
    text = file.read().rstrip()
with open("wlfbd already sent.txt", "w") as file:
    file.write(text+'\n'+alsent)

print('%d users messaged\n%d users mailed\n%d failed\n%d skipped' % (usercnt, usermel, usererr, skipcnt), file=sys.stderr)

# Einde van de miserie
