def big(a,b):
    return a if a>b else b
def gater(a,b,c):
    return big(big(a,b),c)
    
a,b,c=map(int,input("Enter a,b,c: ").split(","))
print(gater(a,b,c))