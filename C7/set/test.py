L=["A",None,"Delwar",5,6,9.1]
def Num(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]
print(Num(L))