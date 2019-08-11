##################
# Code By GogoZin#
##################
import os
sss = str(input("What's System You Using Now ? (termux/linux/debian/kali) : "))
if sss =='termux':
	os.system("apt install figlet &&pkg install python &&pip3 install requests")
else:
	os.system("sudo apt-get install figlet python3 &&pip3 install requests")
import requests
word = str(input("Messege You Want To Show On Terminal : "))
q = "figlet -f slant " + str(word) + "\r\n"
r = requests.get("https://gist.githubusercontent.com/rickdaalhuizen90/d1df7f6042494b982db559efc01d9557/raw/488d28c1b614617025b6dc9d8da1075eedb892d4/.bashrc") # Code By GogoZin
with open('.bashrc', 'wb') as f:
	f.write(q.encode())
	f.write(r.content)
os.system('sudo mv .bashrc ~')
