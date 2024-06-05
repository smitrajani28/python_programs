import random
#     0 1 2
#     s w g
# 0 s D W L
# 1 w L D W 
# 2 g W L D


option=[["Draw", "Win", "Loose"], ["Loose", "Draw", "Win"], ["Win", "Loose", "Draw"]]
while(True):
    c = input("you want to play?(y/n) :")
    if(c == "n" or c=="N"):
        break
    elif(c == "y" or c=="Y"):
        print("enter your choice :")
        choice = int(input("enter you choice :\nsnack=>0 \nwater=>1 \ngun=>2\n"))
        computer = random.randint(0,2)
        print(option[choice][computer])
    else:
        print("invalid input!!!")
