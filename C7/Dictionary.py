#Anything we can store like List


#Create Dictionary
DIC={"Name":"Delwar","Age":23}
#dict Method
DIC1= dict(Name="Delwar",Age=23) #dict key value dont use ""
DIC2={
    "Name":"Delwar", #Must Be use (:) And (,)
    "Movie":None,
    "Age":23,
    "Single":True,
}
print(DIC)
print(DIC1)
print(DIC2)
print(f"{type(DIC)}\n{type(DIC1)}\n{type(DIC2)}")