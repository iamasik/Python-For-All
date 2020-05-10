import random
win=random.randint(1,100)
n=int(input("Guage A number between 1 to 100: "))
for i in range(1,5):
    if n==win:
        print(f"You win!!! and you try {i} times")
        break
    elif n<win:
        print("Too low!!!")
    elif n>win:
        print("Too High!!")
    n=int(input("Try Again: "))
print("You try too many time")