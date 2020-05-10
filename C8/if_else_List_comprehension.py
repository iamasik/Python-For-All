List=["Delwar","Asik",1,5,6,2.0]
List2=[i[::-1] if type(i)==str else (-i) for i in List]
print(List2)