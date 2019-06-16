import random
def generate_Rand(): #for computer input
    return random.randint(1,3)
while True:
    Computer_value = generate_Rand()
    if Computer_value == 1:     #conditions 
        Computer_Move = 's'
    elif Computer_value == 2:  #conditions
        Computer_Move = 'r'
    else:
        Computer_Move = 'p'  #conditions
        
    Player_Move = input("Your Move: (R/S/P)") #player input
    Player_Move = Player_Move.lower()    
    if(Player_Move == 's'):   # checking result
        if(Computer_Move == 's'):
            print("Draw!")
        elif(Computer_Move == 'p'):
            print("Player Wins!")
        elif(Computer_Move == 'r'):
            print("Computer Wins!")
        else:
            print("Wrong Input!")
    elif(Player_Move == 'p'):
        if(Computer_Move == 's'):
            print("Computer Wins!")
        elif(Computer_Move == 'p'):
            print("Draw!")
        elif(Computer_Move == 'r'):
            print("Player Wins!")
        else:
            print("Wrong Input!")
    elif(Player_Move == 'r'):
        if(Computer_Move == 's'):
            print("Player Wins!")
        elif(Computer_Move == 'p'):
            print("Computer Wins!")
        elif(Computer_Move == 'r'):
            print("Draw!")
        else:
            print("Wrong Input!")
    else:
        print("Wrong Input!")
        continue
    close = input("Do you want to Continue?(Y/N)")  #for closing
    close = close.lower()                           #the infinite loop if needed
    if close == 'n':
        break
    else:
        continue

print("TATA!")
exit()

