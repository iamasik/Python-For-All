#get method
#To access Dictionary data
D={
    "Name":"Delwar",
    "Age":23,
}
'''
copy=D["Names"] #show error becouse Names Not in Dictionary
print(copy)
#So we use get method
'''
copy=D.get("Names")
print(copy) #Show None Not Error

if D.get('Name'):
    print("Present")
else:
    print("Not Present")

if D.get('Names'): #Change Name to Names
    print("Present")
else:
    print("Not Present") #Nit present