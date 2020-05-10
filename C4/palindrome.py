name=input("Enter your palindrome check keyword: ")
if name==name[-1::-1]:
    print(f"{name} is Palindrome!!!")
else:
    print(f"{name} is not palindrome!!!")