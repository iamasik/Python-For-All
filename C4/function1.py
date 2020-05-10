# Average funtion

def ave_three(a,b,c):
    return ((a+b+c)/3)

n1,n2,n3=map(int,input("Enter Your n1,n2,n3: ").split(" "))
print(ave_three(n1,n2,n3))