#Without parentheses called Tuple
Tuple="apple","mango","banana"
print(Tuple)
print(type(Tuple))

#Tuple Unpacking
Tuple2=("Dhasik","Malik","karim")
E1,E2,E3=Tuple2
print(E1,E2,E3)

#List Inside Tuple
Tuple3=(1,2,3,["Apple","Mango","Orange"])
Tuple3[3].pop() #Access Tuple Inside List
print(Tuple3)
Tuple3[3].append("Apple")
print(Tuple3)


#Min Max Sum funtion
T=tuple(range(1,11))
print(min(T))
print(max(T))
print(sum(T))