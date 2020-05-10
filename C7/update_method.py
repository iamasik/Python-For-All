DIC={
    'Name':'Delwar',
    'Age':23,
    'Movie':['Coco','Robot','2.0'],
    'Player':['Shakib','Tamim'],
}
more_DIC={
    'city':['Bheramara','Rongpur','Dhaka'],
    'Vill':'candipur',
}
more_DIC2={
    'Name':'Delwar Hossen', #duplicate Name Replace Older data
    'city':['Bheramara','Rongpur','Dhaka'],
    'Vill':'candipur',
}
DIC.update(more_DIC)
print(DIC)

DIC.update(more_DIC2)
print(DIC) #Name Riplaced
