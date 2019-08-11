import os
os.system("sudo apt-get install figlet &&pip3 install requests")

import requests
word = str(input("Messege You Want To Show On Terminal : "))
q = "figlet -f slant " + str(word) + "\r\n"
r = requests.get("https://gist.githubusercontent.com/rickdaalhuizen90/d1df7f6042494b982db559efc01d9557/raw/488d28c1b614617025b6dc9d8da1075eedb892d4/.bashrc")
with open('.bashrc', 'wb') as f:
	f.write(q.encode())
	f.write(r.content)
os.system('sudo mv .bashrc ~')
