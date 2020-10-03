from random import randint
count_pc = 0
count_p1 = 0
print("Welcome to our game ROCK PAPER SCISSORS")
for i in range(10):
    r = randint(1,3)
    if r == 1:
        pc = 'rock'
    elif r == 2: 
        pc = 'paper'
    else :
        pc = 'scissors'
    
    player = input("What is your choice?")    
    if player == 'rock' and pc == 'paper':
        count_pc += 1
    elif player == 'rock' and pc == 'scissors':
        count_p1 += 1
    elif player == 'paper' and pc == 'rock':
        count_p1 += 1
    elif player == 'paper' and pc == 'scissors':
        count_pc += 1
    elif player == 'scissors' and pc == 'rock':
        count_pc += 1 
    elif player == 'scissors' and pc == 'paper':
        count_p1 += 1          

if count_pc > count_p1 :
    print("PC WIN!")
elif count_pc < count_p1 :
    print ("PLAYER WIN!")
else:
    print("severe equal!!")
