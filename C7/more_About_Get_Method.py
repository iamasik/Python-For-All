#If Dictianary Have two same keys
DIC={
    'Name':"Delwar",
    'Age':24,
    'Age':34,
}
print(DIC.get("Age")) #Get Last Age keys First Keys Avoid 
print(DIC.get("Movie")) #Print None
print(DIC.get("Movie","Not Found")) #We can Menual Print Avoid None