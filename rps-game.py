import random

def cmptr_chc_prod():
    n = random.randint(1,3)
    if n ==1:
        return "rock"
    elif n == 2:
        return "paper"
    else:
        return "scissors"

score_user = 0
score_cmp = 0
    
while True:

    user_chc = input("rock? paper? scissors? ")
    cmptr_chc = cmptr_chc_prod()
    print("Computer choice: ", cmptr_chc)
    
    if cmptr_chc == user_chc:
        score_user +=1
    elif user_chc == "rock" and cmptr_chc == "scissors":
        score_user +=1
    elif user_chc == "paper" and cmptr_chc == "rock":
        score_user +=1
    elif user_chc == "scissors" and cmptr_chc == "paper":
        score_user +=1
    else:
        score_cmp +=1
    print("You VS Computer", score_user, "-", score_cmp) 
    
    if score_user == 3 or score_cmp == 3:
        break

if score_user > score_cmp:
    print("You win!")
else:
    print("You lose...")