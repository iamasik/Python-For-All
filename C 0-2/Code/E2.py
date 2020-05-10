Name1,Name2,Name3=input("Enter Your Full Name: ").split(",")
print("Name1: {}\nName2: {}\nName3: {}".format(Name1[-1::-1],Name2[-1::-1],Name3[-1::-1]))      #python 3
print(f"Name1: {Name1[-1::-1]}\nName2: {Name2[-1::-1]}\nName3: {Name3[-1::-1]}")                #Python 3.6