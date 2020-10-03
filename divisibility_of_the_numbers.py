#If you want to calculate the divisibility of one number over another
#Use the following code

num1 = int(input("give me your first number"))
num2 = int(input("give me your seccond number"))

if num1%num2 == 0:
    print("YES , %i is divisible by %i"  %(num1,num2))
else:
    print("NOT divisible")