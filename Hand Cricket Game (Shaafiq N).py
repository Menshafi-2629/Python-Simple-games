from random import *
print("Lets play Hand Cricket")
statement=("Yes","No")

while True:
    options=('0','1','2','3','4','5','6','7','8','9','10')
    parity=("Odd","Even")
    Toss_options=('1','2','3','4','5')
    decision=("Bat","Bowl")
    Player_points=0
    Computer_points=0

    #To put Toss
    while True:
        c=input("\nOdd or Even: ").title()
        if c not in parity:
            print("\nPlease enter a valid option\n")
        else:
            break

    while True:
        y=input("\nPlease enter a Number within 1 to 5 to know who is going to win the toss: ")
        if y not in Toss_options:
            print("\nPlease enter the number within the range\n")
        else:
            break
    z=int(y)
    Toss_computer=choice(Toss_options)
    print("Computers number is:",Toss_computer)
    toss=((int(Toss_computer))+z)%2
    print("\nYou chose:",c)

    if toss!=0:
        toss="Odd"
        print("\nResult: Odd\n")
    else:
        toss="Even"
        print("\nResult: Even\n")

    if c==toss:
        print("You Won the Toss\n")
        while True:
            d=input("Do you Wanna Bat or Bowl: ").title()
            if d not in decision:
                print("\nPlease give a vaild decision\n\n")
            else:
                break
        #If player chose to Bat first
        if d=="Bat":
            while True:
                # Player batting
                while True:
                    p1=input("\n[Player Bating]Please Enter a number between 0 to 10: ")
                    if p1 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p1)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Player_points+=z
                    if z==0:
                        Player_points+=Computer
                    print("\nPlayers points is", Player_points)
                else:
                    Computer_target=Player_points+1
                    print("\nPlayer got out")
                    print("\nPlayers points is", Player_points,"\n\n")
                    print("[Total score of Player is:",Player_points,"\t","Total score need for the Computer to win is:",Computer_target,"]")
                    break

            # Computer batting
            while True:
                while True:
                    p2=input("\n\n[Computer bating]Please Enter a number between 0 to 10: ")
                    if p2 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p2)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Computer_points+=Computer
                    if Computer==0:
                        Computer_points+=z
                    if Computer_points>=Computer_target:
                        break
                    print("\nComputer points is", Computer_points)
                else:
                    print("\nComputer got out")
                    print("\nComputer points is", Computer_points)
                    break
            # Final results
            if Computer_points==Player_points:
                print("\n\n[Total score of Computer is:",Computer_points,"\t","Player points is:",Player_points,"]\n\n")
                print("The Match is draw\n\n")
            elif Computer_target<=Computer_points:
                print("\n\n[Total score of Computer is:",Computer_points,"\t","Player points is:",Player_points,"]\n\n")
                print("The Computer won this match\n\n")
            else:
                print("\n\n[Total score of Computer is:",Computer_points,"\t","Player points is:",Player_points,"]\n\n")
                print("The Player won this match\n\n")
        #If Player chose to bowl first
        else:
            while True:
                # Computer batting
                while True:
                    p1=input("\n[Computer Bating]Please Enter a number between 0 to 10: ")
                    if p1 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p1)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Computer_points+=Computer
                    if Computer==0:
                        Computer_points+=z
                    print("\nComputer points is", Computer_points)
                else:
                    Player_target=Computer_points+1
                    print("\nComputer got out")
                    print("\nComputer points is", Computer_points,"\n\n")
                    print("[Total score of Computer is:",Computer_points,"\t","Total score need for the Player to win is:",Player_target,"]")
                    break
            #Player batting
            while True:
                while True:
                    p2=input("\n\n[Player bating]Please Enter a number between 0 to 10: ")
                    if p2 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p2)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Player_points+=z
                    if z==0:
                        Player_points+=Computer
                    if Player_points>=Player_target:
                        break
                    print("\nPlayer points is", Player_points)
                else:
                    print("\nPlayer got out")
                    print("\nPlayer points is", Player_points)
                    break
            #Final results
            if Computer_points==Player_points:
                print("\n\n[Total score of Player is:",Player_points,"\t","Computer points is:",Computer_points,"]\n\n")
                print("The Match is draw\n\n")
            elif Player_target<=Player_points:
                print("\n\n[Total score of Player is:",Player_points,"\t","Computer points is:",Computer_points,"]\n\n")
                print("The Player won this match\n\n")
            else:
                print("\n\n[Total score of Player is:",Player_points,"\t","Computer points is:",Computer_points,"]\n\n")
                print("Computer won this match\n\n")
    else:
        print("Computer Won the Toss\n")
        Decision_computer=choice(decision)
        print("Computer chooses to",Decision_computer)
        #If Computer chose to Bat first
        if Decision_computer=="Bat":
            while True:
                # Computer batting
                while True:
                    p1=input("\n[Computer Bating]Please Enter a number between 0 to 10: ")
                    if p1 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p1)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Computer_points+=Computer
                    if Computer==0:
                        Computer_points+=z
                    print("\nComputer points is", Computer_points)
                else:
                    Player_target=Computer_points+1
                    print("\nComputer got out")
                    print("\nComputer points is", Computer_points,"\n\n")
                    print("[Total score of Computer is:",Computer_points,"\t","Total score need for the Player to win is:",Player_target,"]")
                    break
            #Player batting
            while True:
                while True:
                    p2=input("\n\n[Player bating]Please Enter a number between 0 to 10: ")
                    if p2 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p2)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Player_points+=z
                    if z==0:
                        Player_points+=Computer
                    if Player_points>=Player_target:
                        break
                    print("\nPlayer points is", Player_points)
                else:
                    print("\nPlayer got out")
                    print("\nPlayer points is", Player_points)
                    break
            # Final results
            if Computer_points==Player_points:
                print("\n\n[Total score of Player is:",Player_points,"\t","Computer points is:",Computer_points,"]\n\n")
                print("The Match is draw\n\n")
            elif Player_target<=Player_points:
                print("\n\n[Total score of Player is:",Player_points,"\t","Computer points is:",Computer_points,"]\n\n")
                print("The Player won this match\n\n")
            else:
                print("\n\n[Total score of Player is:",Player_points,"\t","Computer points is:",Computer_points,"]\n\n")
                print("Computer won this match\n\n")
        #If Computer chose to Bowl first 
        else:
            while True:
                # Player batting
                while True:
                    p1=input("\n[Player Bating]Please Enter a number between 0 to 10: ")
                    if p1 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p1)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Player_points+=z
                    if z==0:
                        Player_points+=Computer
                    print("\nPlayers points is", Player_points)
                else:
                    Computer_target=Player_points+1
                    print("\nPlayer got out")
                    print("\nPlayers points is", Player_points,"\n\n")
                    print("[Total score of Player is:",Player_points,"\t","Total score need for the Computer to win is:",Computer_target,"]")
                    break

            # Computer batting
            while True:
                while True:
                    p2=input("\n\n[Computer bating]Please Enter a number between 0 to 10: ")
                    if p2 not in options:
                        print("\nPlease enter the number within the range\n")
                    else:
                        break
                z=int(p2)
                Computer=int(choice(options))
                print("Computer's choice is:",Computer)
                if z!=Computer:
                    Computer_points+=Computer
                    if Computer==0:
                        Computer_points+=z
                    if Computer_points>=Computer_target:
                        break
                    print("\nComputer points is", Computer_points)
                else:
                    print("\nComputer got out")
                    print("\nComputer points is", Computer_points)
                    break
            # Final results
            if Computer_points==Player_points:
                print("\n\n[Total score of Computer is:",Computer_points,"\t","Player points is:",Player_points,"]\n\n")
                print("The Match is draw\n\n")
            elif Computer_target<=Computer_points:
                print("\n\n[Total score of Computer is:",Computer_points,"\t","Player points is:",Player_points,"]\n\n")
                print("The Computer won this match\n\n")
            else:
                print("\n\n[Total score of Computer is:",Computer_points,"\t","Player points is:",Player_points,"]\n\n")
                print("The Player won this match\n\n")

    while True:
        loop=input("Do you wanna play again ['Yes' or 'No']: ").title()
        if loop not in statement:
            print("\nPlease enter a proper statement\n\n")
        else:
            break
    if loop=="Yes":
        print("\n")
        continue
    else:
        break
