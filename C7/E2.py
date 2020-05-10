D={}
Name=input("Enter Your Name: ")
Age=int(input("Enter Your Age: "))
Movie=input("Enter Your Fev Movie list use ,:").split(",")
D["Name"]=Name
D["Age"]=Age
D["Movie"]=Movie
print(D)

for n1,n2 in D.items():
    print(f"{n1}:{n2}")