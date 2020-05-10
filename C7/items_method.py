DIC={
    'Name':'Delwar',
    'Age':23,
    'Movie':['Coco','Robot','2.0'],
    'Player':['Shakib','Tamim'],
}

Data=DIC.items()
print(Data)
print(type(Data))
#Output Tuple
#[('Name', 'Delwar'), ('Age', 23), ('Movie', ['Coco', 'Robot', '2.0']), ('Player', ['Shakib', 'Tamim'])] 
#Here key  and data tuple print
for key,value in Data:
    print(f"The Key Was{key} and value {value}")