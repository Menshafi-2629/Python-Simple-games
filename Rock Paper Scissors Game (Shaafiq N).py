#Advanced and Fun Version

print("Hi iam AMYD which stands for ''Ask Me,You're Dead'' ")
print("And I am an unbeatable computer💪")
print("you think you can prove me wrong,📢then beat me at the game ")
print("Rock! Paper! Scissors!⚔️\n")

from random import choice

statement=("Yes","No")
options=("Rock","Paper","Scissors")

while True:
    computer_points=0
    player_points=0

    r=int(input("How many rounds do you want to play: "))
    if r==0:
        print("\nLooks like you don't wanna play, ok fine, bye")
        break
    elif r<=0:
        print("\nPlease enter a proper value\n")
        continue
    print("\n")
    while computer_points<r and player_points<r:

        x=input("Please enter your choice: ").title()

        if x not in options:
            print("\nHey!! That's cheating, Enter a valid option😡\n")
            continue

        computer=choice(options)
        print("AMYD's choice is:",computer)

        if x==computer:
            print("\nIt is a tie🙄")
            print("Great escape, Let's play again\n")
        elif (x=="Rock" and computer=="Paper") or (x=="Paper" and computer=="Scissors") or (x=="Scissors" and computer=="Rock"):
            print("\nI win😏")
            print("wanna lose again then Let's play again\n")
            computer_points+=1
        else:
            print("\nOkay fine, you win😒")
            print("but next time I'll beat you and if you're brave enough then let's play again\n")
            player_points+=1


        print("[computer points:",computer_points,"\tPlayer points:",player_points,"]\n")

    if computer_points>player_points:
        print("Ha! I told you I was unbeatable, and you lost this match\n")
    else:
        print("Ok fine!!, I agree you won this match\n")

    while True:
        loop=input("Do you wanna play again: ").title()
        if loop not in statement:
            print("\nPlease enter a proper statement\n")
        else:
            break
    if loop=="Yes":
        print("\n")
        continue
    else:
        break

#Simple Version

"""print("Let's play rock paper scissors\n")

from random import *

while True:
    options=["Rock","Paper","Scissors"]

    x=input("Please enter your choice: ").title()
    if x not in options:
        print("\nPlease enter a valid option\n")
        continue

    computer=choice(options)
    print("Computer's choice is:",computer)

    if x==computer:
        print("\nIt is a tie")
        print("lets paly again\n")
    elif (x=="Rock" and computer=="Paper") or (x=="Paper" and computer=="Scissors") or (x=="Scissors" and computer=="Rock"):
        print("\nYou lose\n")
    else:
        print("\nYou win!\n")"""
