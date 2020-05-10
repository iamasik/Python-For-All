#for i in range(2,11,5):
# print("Hello World!!!")
"""
sum=0
n=input("Enter Your Number: ")
for i in range(0,len(n)):
    sum+=int(n[i])
print(sum)
"""
name=input("Enter your name: ").lower()
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f" Here {name[i]} : {name.count(name[i])}")
        temp+=name[i]


 