n=int(input("Enter Your Number: "))
f1=0
f2=1
sum=0
for i in range(n):
    print(f1)
    sum=f1+f2
    f1=f2
    f2=sum
