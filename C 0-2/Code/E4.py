Name,Alpha=input("Enter Your Name: \n Use ',' \n Enter Your Alphabet: ").split(",")
Name=Name.replace(" ","")
print(f"Your Name Length {len(Name.strip())} \n Simile Alphbet: {Name.lower().count(Alpha.strip().lower())}")