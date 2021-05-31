import random
lis=["stone","paper","scissor"]

your_point=0
pc_point=0
turn=0
chance=10

while turn<chance:
    inp=input("enter your choice:")
    randoms=random.choice(lis)

    if inp==randoms:
        print("match withdraw both earns 0 point")
    elif inp=="stone" and randoms=="paper":
        pc_point+=1
        print("your=stone ,pc=paper")
        print("pc wins")
        print(f"your point={your_point} and pc point={pc_point}")
    elif inp=="stone" and randoms=="scissor":
        your_point+=1
        print("your=stone ,pc=scissor")
        print("you win")
        print(f"your point={your_point} and pc point={pc_point}")
    elif inp=="paper" and randoms=="scissor":
        pc_point+=1
        print("your=paper and pc=scissor")
        print("pc wins")
        print(f"your point={your_point} and pc point={pc_point}")
    elif inp=="paper" and randoms=="stone":
        your_point+=1
        print("your=paper and pc=stone")
        print("you win")
        print(f"your points={your_point} and pc point={pc_point}")
    elif inp=="scissor" and randoms=="stone":
        pc_point+=1
        print("your=scissor and pc=stone")
        print("pc win")
        print(f"your point={your_point} and pc point={pc_point}")
    elif inp=="scissor" and randoms=="paper":
        your_point+=1
        print("your=scissor and pc=paper")
        print("you win")
        print(f"your point={your_point} and pc point={pc_point}")
    turn+=1
    print("number of chances left=",chance-turn)
           
        
print("GAME OVER")
print("your total point=",your_point)
print("pc's total point=",pc_point)
    
