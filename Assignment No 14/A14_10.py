Num1=int(input("Enter the 1st Number=>"))
Num2=int(input("Enter the 2nd Number=>"))
Num3=int(input("Enter the 3rd Number=>"))


Max=lambda Num1,Num2,Num3 : max(Num1,Num2,Num3)

result=Max(Num1,Num2,Num3)

print("Greater Number is =>",result)