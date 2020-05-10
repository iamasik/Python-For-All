#Reverse String by comprehension
List=["abc","xyz","hft"]
Rev_Stri=[i[-1::-1] for i in List]
print(Rev_Stri)

#using function
def Rev_Str(l):
    return [i[::-1] for i in l]
print(Rev_Str(List))