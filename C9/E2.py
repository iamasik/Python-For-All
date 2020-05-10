Names=["Delwar","Hossen"]
def Rev_T(name,**kwargs):
    if kwargs["Rev"]==True:
        return [i[::-1].title() for i in name]
    else:
        return [i.title() for i in name]

print(Rev_T(Names,Rev=True))
print(Rev_T(Names,Rev=False))