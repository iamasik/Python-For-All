List=[[1,2,3,4],[5,6,7],[8,9,0]] #Its Called 2D List
#print List Element
for i in List:
    print(i)
print()

#print List Every Element
for i in List:
    for j in i:
        print(j)
print()

#print Only Slected Element All List
for i in List:
    if i==List[1]:
        for j in i:
          print(j)
    else:
        pass