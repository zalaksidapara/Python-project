import string
import secrets
import random 
x=int(input("enter length of password: "))

symbols = ['*', '%', '£'] # Can add more

password = ""
a = secrets.choice(string.ascii_lowercase)
b = secrets.choice(string.ascii_uppercase)
c = secrets.choice(string.digits)
d = secrets.choice(symbols)
ch=[a,b,c,d]
for _ in range(x):
    password+=secrets.choice(ch)
print("Your password is : \n",password)