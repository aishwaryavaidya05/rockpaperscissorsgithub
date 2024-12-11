import random
options=["rock","paper","scissors"]
def play():
    
    n=str(input("enter choice (rock, paper or scissors):")).lower()
    while n not in options:
            print("invalid input. please enter from the given choices")
            n=str(input("enter choice (rock, paper or scissors):")).lower()
    ans=random.choice(options)
    print(ans)
    if n==ans:
        print("it's a tie")
    elif n=="rock" and ans=="scissors":
        print("you win")
    elif n=="scissors" and ans=="paper":
        print("you win")
    elif n=="paper" and ans=="rock":
        print("you win")
    else:
        print(" you lose, better luck next time")
    a=str(input("do you want to play again? (y/n)")).lower()
    while a!="y" and a!="n":
            print("please enter valid input y or n")
            a=str(input("do you want to play again? (y/n)")).lower()
    if a=="y":
        play()
    elif a=="n":
        print("thank you for playing")
play()
        
