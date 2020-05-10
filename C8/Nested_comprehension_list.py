List=[[i for i in range(1,4)] for j in range(6)]
print(List)


l = [1, 2, 3, "Asik",None]
List2=[f'{i} integer' if type(i) == int else f'{i} String' if type(i) == str else f'{i} Other Type' for i in l]
print(List2)