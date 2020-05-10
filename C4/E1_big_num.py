def big_small(a,b):
    return f"Big Number {a}" if a>b else f"Small Number {b}"
n1,n2=map(int,input("Enter n1 space n2: ").split(" "))
print(big_small(n1,n2))