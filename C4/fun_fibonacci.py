def fibo(n):
    f1=0
    f2=1
    for i in range(n):
        print(f1, end=" ") # No need return Becouse only one valu return it
        sum=f1+f2
        f1=f2
        f2=sum
n=int(input("Enter your Number: "))
fibo(n)