Age=int(input("Enter Your Age: "))
if Age<=0:
    print("You Are Not Allowed!!!")
elif 0<Age<=3:
    print("Yor Are : Freeeeee!!!")
elif 3<Age<=10:
    print("Ticket Price: 100")
elif 10<Age<=60:
    print("Ticket Price : 250")
else:
    print("Ticket Price : 200")