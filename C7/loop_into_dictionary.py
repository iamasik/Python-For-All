#Values Method 
DIC={
    "Name":"Delwar",
    "Age":23,
    "Movie":["coco","Robot","Hulk"]
}
print(DIC)
print(DIC.values()) #Output Like List But its not list we can looping like list  those data
print(type(DIC.values())) #<class 'dict_values'>

print("\n \n")

#For Loop For Keys Print
for item in DIC: #Only print key name
    print(item,end=" ")
print()
#OR
#Keys Method
for item in DIC.keys():
    print(item,end=" ")
print("\n \n")

#For loop for values print
for item in DIC.values(): #Only print Values
    print(item,end=" ")
print()
#or
for item in DIC:
    print(DIC[item],end=" ")
print("\n \n")




DIC_keys=DIC.keys()
print(DIC_keys) #But Its Not List