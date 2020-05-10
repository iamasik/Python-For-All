List=["Asik","Delwar",'Coco',4,6,2.0,True,(1,2,3,6)]
DIC2={i:("String" if type(i)==str else "Integer" if type(i)==int else "Boolean" if type(i)==bool else "Float" if type(i)==float else "Tuple" if type(i)==tuple else "Other") for i in List}
print(DIC2)



# a_list = ['name', 'country', 'career']
# b_list = ['Maateen', 'Bangladesh', 'TeleTalk']
# my_dict =zip(a_list, b_list)
# print(type(my_dict))
# print(list(my_dict))
# D={}
# for i,j in zip(a_list, b_list):
#     D[i]=j
# print(D)