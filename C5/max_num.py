def large(l):
    max=l[0]
    for item in l:
        if item > max:
            max=item
    return max

List=[99,55,77,22,33]
print(large(List))