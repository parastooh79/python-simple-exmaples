# We want to check with regex , the correct email address and mobile number entered
import re
name = input("what's your name?")
email = input("what's your email adress? ")
phone = input("what's your phone number? ")

ech = re.search(r'.+@.+\..{2,3}',email)
if ech == None:
    print("dear %s your email adress is invalid" %name)
else:
    print("your email is ok")

pch = re.search(r'^\d{11}',phone)
if pch == None:
    print("dear %s your phone number is invalid" %name)
else:
    print("your phone number is ok")
