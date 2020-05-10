def pal(word):
    return  word==word[-1::-1]
name=input("Enter keyword: ")
print(pal(name))