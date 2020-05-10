#With pop and append Method
def Reverse(l):
    n=[]
    for i in range(len(l)):
        n.append(l.pop())
    return n
#with reverse method
def rev(l):
    l.reverse()
    return l

#with Index Method
def rev_index(l):
    return l[-1::-1]

List=list(range(1,12))
List2=list(range(1,12))
List3=list(range(1,12))
print(Reverse(List))
print(rev(List2))
print(rev_index(List3))