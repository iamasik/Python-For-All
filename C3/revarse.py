name=input("Enter your revarse number: ")
print(name[-1::-1])
C=len(name)
for i in range(C-1,-1,-1):
    print(name[i], end="")