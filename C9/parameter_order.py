def order(Normal,*args,default="Unknown",**kwargs):
    print(Normal)
    print(args)
    print(default)
    print(kwargs)
List=[1,2,3,5,4]
DIC={"Name":"Asik","Age":23}
order(3,*List,**DIC)