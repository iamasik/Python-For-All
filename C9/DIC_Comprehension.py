DIC={i:i**2 for i in range(1,10)}
print(DIC)

#How Many Same Charector in A String
A="Delwar Hossen Asik"
DIC={i:A.count(i) for i in A}
print(DIC)

#Two List To Dictionary
D1=list(range(11,20))
D2=list(range(1,10))
D={i:j for i,j in zip(D1,D2)}
print(D)