Tuple=tuple(range(1,8))
print(Tuple)

#Tuple to list to tuple
List=list(Tuple)
print(List)
List.append(6)
Tuple=tuple(List)
print(Tuple)

Tuple2=tuple(range(1,8))
Str=str(Tuple2)
print(Str)
print(type(Str))

#Join Tuple
T1=(1,2,3,4)
T2=(5,6,7,8)
T3=T1+T2
print(T3)

#Delete tuple
del T1
print(T1) #Error Becouse Tuplw Doesn't Exist