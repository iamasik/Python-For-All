win=43
n=int(input("Enteer your Number: "))
g=1
game="" #Data nai
while not game:
    if win==n:
        print(f"you win!!!! and you try {g} times")
        game="Game Over" #Data asay
    else:
        if win>n:
            print("too low")
        else:
            print("too high")
        g+=1
        n=int(input("try again: "))