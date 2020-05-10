DIC={
    'Name':'Delwar',
    'Age':23,
    'Movie':['Coco','Robot','2.0'],
    'Player':['Shakib','Tamim'],
}

#Add
DIC['Captain']="Masrafi" 
print(DIC)

#Pop method
#DIC.pop() #Error Becouse its not like list atleast 1 argument pass
#print(DIC)

poped=DIC.pop("Name")
print(poped) #Return data type
print(type(poped))
print(DIC) #Name Removed
print()

#poped item method
poped_item=DIC.popitem()
print(poped_item) #Tuple Return
print(DIC) #Last item Removed