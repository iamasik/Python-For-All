#for Create a dictionary
#Like-------> DIC={'Name':'Unknown',"Age":'Unknown'}
DIC=dict.fromkeys(['Name','Age','Hight'],'Unknown') #Auto Create
print(DIC)
# Also use tuple
DIC2=dict.fromkeys(('Name','Age','Hight'),'Unknown')
print(DIC2)

#Why Useing List or Tuple
DIC3=dict.fromkeys("Name",'Unknown')
print(DIC3) #Print Like {'N': 'Unknown', 'a': 'Unknown', 'm': 'Unknown', 'e': 'Unknown'}

DIC4=dict.fromkeys(range(1,11),"Unknown")
print(DIC4)