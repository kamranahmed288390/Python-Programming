import random

'''
1 for Snake
-1 for Water
0 for Gun
'''
computer = random.choice([-1,1,0])
youstr = input("Enter your choice: ")

youDict = {"s":1, "w":-1, "g":0}

Reversedict = {1: "Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]

print(f"You choose {Reversedict[you]} \n Computer choose {Reversedict[computer]}")


if (computer==you):
    print("It's a draw")

else:
    if (computer==-1 and you==1):

     print("You win!")

    elif (computer==-1 and you==0):
     print("You lose!")

    elif (computer==1 and you==-1):
     print("You lose!")

    elif (computer==1 and you==0):
     print("You win!")


    elif (computer==0 and you==1):
     print("You win!")

    elif (computer==0 and you==-1):
     print("You lose!")

    else:
     print("Something went wrong")


