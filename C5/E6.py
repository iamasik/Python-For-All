#Check How Many Inside List

List=[1,2,3,[1,2,3],[4,5,6]]

def Check_List(l):
    c=[]
    for item in l:
        if type(item)==list:
            c.append(item)
    return len(c)

print(Check_List(List))