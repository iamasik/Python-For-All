Fast_Name,Last_Name,B_Day,B_Month,B_year,Age=input("Input Your Fast_Name: \nLast_Name: \nB_Day: \nB_Month: \nB_year: \nAge: \nUsing Commna ").split(",")
Num1,Num2,Num3=input("Input Your Three Number").split(",")
Ave=(int(Num1)+int(Num2)+int(Num3))/3
print(f"{Fast_Name} {Last_Name} Your Birth Date {B_Day}-{B_Month}-{B_year} And Your Age IS {Age}")
print("{} {} Your Birth Date {}-{}-{} And Your Age IS {}".format(Fast_Name,Last_Name,B_Day,B_Month,B_year,Age))
print(f"The Avarage Is {Ave}")