#Set If Condition
# s={"a",1,2,3.0,(5,6)}

# if "a" in s:
#     print("Present")
# else:
#     pass

#Set Looping
# for item in s:
#     print(item)

#Set Union And Intersection And Difference
S1={2,3,6,5,4}
S2={1,2,5,6,9}

#Union
U=S1 | S2
U1=S1.union(S2)
print(f"{U} \n{U1}")

#InterSect
I=S1 & S2
I1=S1.intersection(S2)
print(f"{I}\n{I1}")

#Difference
D=S1.difference(S2)
print(D)