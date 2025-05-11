num1 = float(input("Enter First Side Of Triangle:")) 
num2 = float(input("Enter Second Side Of Triangle:"))
num3 = float(input("Enter Third Side Of Triangle:"))
if(num1 + num2 + num3 == 180):
    print("Valid Triangle.")
    if(num1 == num2 == num3):
        print("Equilateral Triangle.")
    elif(num1 == num2 or num2 == num3 or num1 == num3):
        print("Isosceles Triangle.")
    else:
        print("Scalene Triangle.")
else:
    print("Not A Valid Triangle.")
