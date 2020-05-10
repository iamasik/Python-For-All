temp=input("Enter tempuratur value with 30C or 45F: ")
d=temp[-1].upper()
s=int(temp[:-1])
if d=="C":
    r=int(32+((9*s)/5))
    print(f"Fharenhite scale is :::: {r}°F")
elif d=="F":
    r=int(5*((s-32)/9))
    print(f"Celcius scale is :::: {r}°C")
else:
    print(f"Wrong input ==> {temp} < try again this format 40C or 50F>")