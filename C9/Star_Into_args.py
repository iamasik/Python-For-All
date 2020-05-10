#To Flexible Function
def Total(*args):           #All Data Make Tuple Like(1,2,3)
    Sum=0
    for i in args:
        Sum+=i
    return Sum
print(Total(2,3,6,5,89,8))