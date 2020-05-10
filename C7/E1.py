#Cube Finder
def cube_find(l):
    D={}
    for item in range(1,l+1):
        D[item]=item**3
    return D

n=int(input("Enter cube Value: "))
print(cube_find(n))