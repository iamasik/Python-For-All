#Dictionary Do not have indexing
#like
DIC={"Name":"Delwar","Address":"Bheramara","Age":23}
# print(DIC[0]) #Error Becoude Dictionary do not have Indexing

#So we using key value 
#Name,Address,Age Called Key value which stored the data
print(DIC["Name"]) #Mustbe use "" qouation

#List Inside Dictionary
DIC2={"Name":"Asik","Movie":["Coco","Tom",None]}
#How To Access List Data
print(DIC2["Movie"][0:2])


#get method
print(DIC.get('Name'))