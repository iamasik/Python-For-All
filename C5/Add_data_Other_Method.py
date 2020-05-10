#append #insert #extend
Program1=["Java","C#"]
Program1.insert(0,"Python")
#Inset Method (Position Num, Data)
print(Program1)

#How To Combine Two List
Program2=["Go","C","Ruby"]
Program=Program1+Program2
print(Program)

#Extend Method Add A List TO other list
Program1.extend(Program2)
print(Program1)

#If We Use Append Method to add A list To other list
Program1.append(Program2)
print(Program1) # Add also With Brakets Full List