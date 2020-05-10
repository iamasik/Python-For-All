D={
    "Name":"Delwar",
    "Age":23,
}

#Copy Method
D1=D.copy()
print(D1)
print(D1 is D) #print false becouse diffrent location
print(D1 == D) #print true becouse check same value or not

D2=D #Its no copy its same access one location
#Clear Method
D.clear()
print(D)
print(D2) #Output Empty 
# So do not use =
#Must use copy