n=int(input("Enter maximum pattarn number: "))
e=""
for i in range(n,0,-1):
    e+=" "
    print(end=e)
    for j in range(i):
        print("* ",end=(""))
    print()
for i in range(2,n+1):
    for j in range(i):
        print("* ",end=(""))
    print()
    