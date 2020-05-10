#Set Immuatble
#Set unorderd Collection
#Set Create
# s={1,2,3,5}
# s1=set(range(1,6))
# print(s)
# print(s1)

#Duplicate Not Allow
# s={1,2,3,5,6,6,4,4,8}
# print(s)

#Add method (Add A item)
#s={} #Not Allow Becouse its Dictionary without item
# s=set()
# s.add(5)
# s.add(6)
# print(s)

#List Duplicate Remove
# L=[1,2,3,6,5,9,9,8,4,4,7]
# s=set(L)
# s=list(s)
# print(s)

#Remove Method
# s={1,2,3,6,5}
# s.remove(5)
# print(s)

#Remove method if a item not present set output error
# s={1,2,3,6,5}
# s.remove(9) #9 Not Present
# print(s) #Error

#Remove Error Handel
#Discard Method
# s={1,2,3,6,5}
# s.discard(6) #6 removed
# print(s)

#Pop method
# s={1,2,3,6,5}
# s.pop()
# print(s) #Poped Last Method

#del Statement
# s={1,2,3,6,5}
# del 
# print(s) #Error Becouse the set is no longer

#Error Avoid
# s={1,2,3,6,5}
# s.discard(9) #9 Not Present in the set
# print(s) #Still Output not error

#copy method
# s={1,2,3,6,5}
# s2=s.copy()
# print(s2)

#Clear Method
# s={5,6,9,8,4}
# s.clear()
# print(s)

#Sort Function
# s={1,2,3,6,5,9,7,8}
# print(sorted(s))

#Sum method
# s={1,2,3,6,5,9,7,8}
# Sum=sum(s)
# print(Sum)

#Max Min function
# s={1,2,3,6,5,9,7,8}
# print(max(s),min(s))

#What We Store inside set
# s={1,2,1.0,1.1,"Asik",True,None,(9,8)} 
#int,float,string,None,tuple
# print(s)

#What We Didn't Store
# s={{1:2},[5,6]}  #List , Dictionary
# print(s)

#Update Method
# s1={6,5,8,7,9}
# s2={9,8,2,14,7}
# s1.update(s2)
# print(s1)

#Also Use Length Function

