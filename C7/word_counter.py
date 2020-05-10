def word_count(n):
    #No Need Temp variable to store check item like list
    #Becouse Dictionary Removed Overwrite Item
    D={} 
    for item in n: 
        D[item]=n.count(item)
    return D

Name="Delwar Hossen"
print(word_count(Name.lower())) 

#Importent Dictionary Unorderd 
#Outpur Serial Unordered