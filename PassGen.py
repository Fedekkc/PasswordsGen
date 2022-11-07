
import string, secrets
from random import randint
from time import sleep
password = ""
num = 0

for i in range(20):
	num = randint(0,10)
	if num % 2 == 0:
		password += secrets.choice(string.ascii_letters)
	elif num % 3 == 0:
		password += secrets.choice(string.digits)
	else:
		password += secrets.choice(string.punctuation)

	

print(password)
