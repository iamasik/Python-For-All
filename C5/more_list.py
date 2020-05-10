#Genarate List
List=list(range(1,11))
print(List)

#pop Return
print(List.pop()) 
#Last Value Return Becouse poped data don't lost
print(List)


List1=[1,2,3,6,5,4,8,9,7,1]
#list index
print(List1.index(8,2,len(List1))) 
print(List1.index(1,2,len(List1))) #find position 
#List1.index(Finded value,Start Position,End Position)

#Pass List In A Function
List0=[1,2,3,6,5,4,8,9,7,1]
def neg(l):
    neg=[]
    for i in l:
        neg.append(-i)
    return neg
print(neg(List0))
