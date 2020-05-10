# But we are not using this method
# not change golobal into function
#only time weast

X=7 #Global Variable
Z=8
def var():
    global Z #using global variable into fuction
    Z=55
    y=5 #local variable
    return y
print(Z) #Before Call var() function global variable not chaneg Z=8
print(X) #X global Print 7
print(var()) #function call print 5
print(Z) #After call Var() function call (global Z) value change Z=55
print(y)  #not work direct local variable call