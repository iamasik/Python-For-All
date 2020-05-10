#List Comprehension
#Append 1 to 10 Square
#Simple method
# List=[]
# for i in range(1,10):
#     List.append(i**2)
# print(List)

#Now List Cpmprehension
List=[(i**2) for i in range(1,10)]
print(List)

#for negetive number 
#Simple Method
# List=[]
# for i in range(1,10):
#     List.append(-i)
# print(List)

#Now List comprehension
Lisi1=[-i for i in range(1,10)]
print(Lisi1)