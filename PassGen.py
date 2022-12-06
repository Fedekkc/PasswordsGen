
import string, secrets
from random import randint

password = ""
num = 0
longpass = int(input("How long do you want your password to be? - "))

for i in range(longpass):
	num = randint(0,10)
	if num % 2 == 0:
		password += secrets.choice(string.ascii_letters)
	elif num % 3 == 0:
		password += secrets.choice(string.digits)
	else:
		password += secrets.choice(string.punctuation)

	
print("-> Password Generator - Federico Cacace")
print("-> @Fedekkc on Github | @Fedekkc_ on IG")
print("Your password: " + password)
