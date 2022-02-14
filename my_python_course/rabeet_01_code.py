import random
print("Rock Paper Sciosor")
print("GAME RULE!")
print("R for Rock   1: Rock Can win if Scisor \nP for Paper  2: Paper Can win if Rock\nS for Scisor 3: Scisor Can win if paper")

options=["R","P,","S"]
user_wins=0
comp_wins=0
round=1
r=int(input("How many round you want to play?\n"))

while round <= r:
    print(f"Round : {round}")
    print("Options Are : R, P ,S")
    input_by_user=input("Chose Your Options\n")
    input_by_user=input_by_user.upper()
    input_by_comp= random.choice(options)
    if input_by_comp =="R":
        if input_by_user =="P":
            print("Paper cover your Rock")
            user_wins=+1
           
        elif input_by_user =="S":
            print("Scisor is Smashed by Rock")
            comp_wins=+1   

    if input_by_comp =="P":
        if input_by_user =="S":
            print("Your Scisor cut the paper")
            user_wins=+1
            
        elif input_by_user =="R":
            print("Rock is coverd by paper")
            comp_wins=+1     

    if input_by_comp =="S":
        if input_by_user =="R":
            print("Your Rock Smashed the sciosor")
            user_wins=+1
            
        elif input_by_user =="P":
            print(" Your paper is cut by Scisor")
            comp_wins=+1     

    if user_wins>comp_wins:
        print(f"Congrutualation you win the Round {round}\n")
    elif comp_wins>user_wins:
        print(f"Better Luck Next Time for the Round {round}\n") 
    else:
        print("Round Has Drawn")

    round+=1     

if user_wins>comp_wins:
    print("Congrutualation You Win The Game ")
elif comp_wins>user_wins:
    print("Better Luck Next Time for the game") 

else:
    print(f"Game has Drawn ,{r} ")

print("Your point is , ",user_wins)
print("Comp score is  , ",comp_wins)