#Print Only Number by string
List=[True,None,False,1,2.0,3]
def num(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]
print(num(List))