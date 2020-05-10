def Power_List(power,*args):
    if args:
        return[i**power for i in args]
    else:
        return "You didn't passed any value"
Num=(1,2,3,6,5,4,8,7)
Num2=()
print(Power_List(3,*Num)) #Pass *Num Unpacked tuple
print(Power_List(3,*Num2)) #Pass *Num2 Empty tuple
