def DIC(**kwargs):               #Read A Dictionary And Sotre As Dictionary
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}:{v}")
DIC(Name="Delwar",Age=25)

DIC1={
    "Name":"Delwar",
    "Age":23,
    "Movie":"COCO"
}
def DICT(**kwargs):
    for k,v in kwargs.items(): 
        print(f"{k}:{v}")
DICT(**DIC1)
