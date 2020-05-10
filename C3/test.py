n=int(input("Enter maximum pattarn number: "))
e=""
f=""
for i in range(n,0,-1):
    e+=" "
    print(end=e)
    for j in range(i):
        print("*",end=(" "))
    print()
l=len(e)
for i in range(1,n+1):
    f=e[0:l]
    print(end=f)
    for j in range(i):
        print("*",end=(" "))
    print()
    l=len(e)-i

    
    
