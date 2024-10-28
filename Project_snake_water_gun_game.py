import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youDict = {"s" : 1 , "w" : -1, "g" : 0}
reverseDict = {1 : "snake" , -1 : "water" , 0 : "gun" }

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if computer == you:
    print("It is Draw ")

else:
    if computer == -1 and you == 1:
        print("you Win! ")

    elif computer == -1 and you == 0:
        print("you Lose! ")

    elif computer == 1 and you == -1:
        print("you Lose! ")

    elif computer == 1 and you == 0:
        print("you Win! ")

    elif computer == 0 and you == -1:
        print("you Win! ")

    elif computer == 0 and you == 1:
        print("you Lose! ")

    else:
        print("Something went wrong! ")