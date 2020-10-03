for i in range(1000):
    i += 1
    if i%3 == 0:
        inp = input("Count: ")
        if inp == 'hope' or inp == 'HOPE' or inp == 'Hope' or inp == 'H' or inp == 'h':
            print('OK')
        else:
            print('YOU LOST!!!!')
            break     
    else:
        inp = int(input("Count: ")
        if inp == i:
            print("OK")
        else:
            print('YOU LOST!!!')                
            break
