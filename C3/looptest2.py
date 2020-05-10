# DELWAR HOSSEN
name=input("Enter Your Name: ").lower()
i=0
temp=""
while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} = {name.count(name[i])}")
    i+=1
