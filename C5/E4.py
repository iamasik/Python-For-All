#Filter Odd And Even

def odd_even(l):
    odd=[]
    even=[]
    for item in l:
        if (item%2==0):
            even.append(item)
        else:
            odd.append(item)
    n=[even,odd]
    return n
List=[1,2,3,4,5,6,7,8,9]
print(odd_even(List))