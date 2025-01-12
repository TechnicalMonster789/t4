#Game
import random
lis=["stone","paper","scissor"]
human_point=0
comp_point=0
no_of_chance=0
chance=10


for i in range(0,chance):
    comp_choice=random.choice(lis)
    user_choice=input("enter your choice: ")
    print(f"computer choice: {comp_choice}")

    if comp_choice==user_choice:
        print("Tie both 0 point each \n")

    elif comp_choice=="stone" and user_choice=="paper":
        comp_point=comp_point+1
        print("Computer won!"," \n the point of computer is: ",comp_point)
    elif comp_choice=="stone" and user_choice=="scissor":
        comp_point==comp_point+1
        print("Computer won!"," \n the point of computer is: ",comp_point) 
    elif comp_choice=="paper" and user_choice=="stone":
        human_point=human_point+1
        print("You won!\n","Your point is: ",human_point)
    elif comp_choice=="paper" and user_choice=="scissor":
        human_point=human_point+1
        print("You won!\n","Your point is: ",human_point)
    elif comp_choice=="scissor" and user_choice=="stone":
        human_point=human_point+1
        print("You won!!\n","Your point is: ",human_point)
    elif comp_choice=="scissor"  and user_choice=="paper":
        comp_point=comp_point+1
        print("Computer won!\n","Computer point is: ",comp_point)
    else:
        print("invalid input for STONE PAPER SCISSOR Game")  


    no_of_chance=no_of_chance+1    
    print(f"{chance-no_of_chance} is left out of {chance} \n ")

print("Game over")

if comp_point==human_point:
    print("Tie")

elif comp_point>human_point:
    print("Computer won the game!!! and you lo0se")

elif human_point>comp_point:
    print("You won the game!! and computer loose")

else:
    print("you won and computer loose")

print(f"Your point is{human_point} and Computer point is{comp_point}")    

                               