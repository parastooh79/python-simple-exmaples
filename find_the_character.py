#If you have a string and you want to find a character in it
#Use the following code
#without regex

txt = input('give me your text?  ')
ch = input ('what word are you looking for?  ')

op = txt.find(ch)

if op == -1:
    print("sorry I didn't found it :)")
else:
    print("hoora It's starting on letter %i " %op)
