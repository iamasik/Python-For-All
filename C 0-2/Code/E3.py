Name,Apha=input("Enter Your Name: ").split(",")
print(f"Name Length: {len(Name)}")
print(f"Similler Word: Lower Case: {Name.lower().count(Apha)} Upper Case: {Name.upper().count(Apha)}")    #Case inSensitive