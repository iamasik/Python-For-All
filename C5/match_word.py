def match_words(l):
    Count=0
    for item in l:
        if (len(item)>=2) and (item[0]==item[-1]):
            Count+=1
    return Count

List=['abc', 'xyz', 'aba', '1221']
print(match_words(List))