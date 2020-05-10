#Two List print Common number

def common(l1,l2):
    n=[]
    for item in l1:
        if item in l2:
            n.append(item)
    return n
List1=[1,2,5,6,9]
List2=[2,3,6,5,8,4,6]
print(common(List1,List2))