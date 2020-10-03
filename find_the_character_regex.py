#If you have a string and you want to find a character in it
#Use the following code
#with regex

import re
txt = input('give me your text?  ')
ch = input ('what word are you looking for?  ')

op = re.search(ch,txt)

if op == None:
    print("sorry I didn't found it :)")
else:
    print(op.span())