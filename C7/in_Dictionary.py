DIC={"Name":"Delwar","Age":23,"Movie":["coco","mowna"]}
if "Name" in DIC:
    print("Ok")
else:
    print("Not Ok")


#Value Not Check
if "Delwar" in DIC: #Not Ok Becouse "Delwar" in to "Name"
    print("Ok")
else:
    print("Not Ok")

#For Value Check
#Values method
if ("Delwar" or 23) in DIC.values():
    print("OK")
else:
    print("Not Ok")