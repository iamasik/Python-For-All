#Find Max Min
List=[55,44,99]
def min_max(l):
    print(f"Minimum Value Is= {min(l)}")
    print(f"Maximum Valie Is= {max(l)}")

min_max(List)

#Find Max Min Sub
List2=[54,44,99]
def min_max(l):
    return max(l) - min(l)

print(min_max(List2))