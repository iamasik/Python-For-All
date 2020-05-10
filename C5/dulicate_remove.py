def duplicate(l):
    n=[]
    for item in l:
        if item  not in n:
            n.append(item)
    return n

List=['abc', 'xyz', 'abc', '121','123','121']
print(duplicate(List))