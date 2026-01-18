import pyfiglet  # type: ignore
heading = pyfiglet.figlet_format("Stone Paper Sisser Game",font ="smslant")
print(heading)

while True:
    # stone Paper Sisser Game

    import random
    computer = random.choice([0,1,2])

    #print(computer)
    dict={ 0 : "Stone",
        1 : "Paper",
        2 : "Sisser"}
    
    #user
    print("\n a: Stone\n s: Paper\n d: Sisser")
    
    n=input("Choose between a,s,d: ")

    new_dict={"a" : "Stone",
            "s" : "Paper",
            "d" : "Sisser"}

    print(f"Computer choose: {dict[computer]}")
    print(f"You choose: {new_dict[n]}")

    #print(dict)
    #print(new_dict)

    if(dict[computer]==new_dict[n]):
        print("It's a draw, try again")
    else:
        if(computer==0 and n=="s"):
            print("You won")
        elif(computer==0 and n=="d"):
            print("Computer won")
        elif(computer==1 and n=="a"):
            print("Computer won")
        elif(computer==1 and n=="d"):
            print("You won")
        elif(computer==2 and n=="a"):
            print("You won")
        elif(computer==2 and n=="s"):
            print("Computer won")