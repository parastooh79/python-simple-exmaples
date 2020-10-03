# divisibility on 2 & 3
num = int(input("give me your number? "))

two = num%2
three = num%3

if two == 0 and three == 0:
    print("BOTH")
elif two == 0 or three == 0:
    print("ONE")
else:
    print("NEITHER")   