def multiply(*args):        #Tuple (2,3,6,5,4)
    #Its Called Perameter
    multi=1
    for i in args:
        multi*=i
    return multi
print(multiply(2,3,6,5,4)) #multiply (2,3,6,5,4)
#Its Called Argument

#Now with Normal Perameter
def multiply(Num1,*args):        #Num1=2 args=Tuple (3,6,5,4)
    #Num1 One perameter *args One Perameter
    multi=1
    for i in args:
        multi*=i
    return multi
print(multiply(2,3,6,5,4))      #multiply Only (3,6,5,4) without 2

#If No Argument Pass 
def multiply(Num1,*args):
    multi=1
    for i in args:
        multi*=i
    return multi
print(multiply()) #Error Becouse Num1 must be fillup but *args create empty tuple()

#If Num1 Perameter after *args 
def multiply(*args,Num1):
    multi=1
    for i in args:
        multi*=i
    return multi
print(multiply(2,3,6,5,4)) 
#Its Also Error Becouse all inputed argument going to args tuple so num1 have no argument