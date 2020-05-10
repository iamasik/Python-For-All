def big(a,b,c):
    if a>b and a>c:
            return f"{a} Big"
    elif b>c:
        return f"{b} Big"
    else:
        return f"{c} Big"
n1,n2,n3=map(int,input("Enter n1 space n2 space n3: ").split())
print(big(n1,n2,n3))