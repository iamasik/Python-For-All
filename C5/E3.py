List=["Apple","Mango","Orange"]
def Item_rev(l):
    n=[]
    for item in l:
        n.append(item[-1::-1])
    return n
print(Item_rev(List))
