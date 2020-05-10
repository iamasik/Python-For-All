List=[1,2,3,6,5,4]
def Multiply(*args): #Now Tuple Has One Value List Like ([1,2,3,6,5,4])
    multi=1
    for i in args:
        multi*=i
    return multi
print(Multiply(List)) #Nothing Happening 
# So How We Unpack

# To Unpack The List As A Argument
List=[1,2,3,6,5,4] 
def Multiply(*args): #Now List Unpacked (1,2,3,6,5,4)
    multi=1
    for i in args:
        multi*=i
    return multi
print(Multiply(*List)) #Use Unpaking (*) *List