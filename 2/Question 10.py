num1 = float(input("Enter First Angle Of Triangle:")) 
num2 = float(input("Enter Second Angle Of Triangle:"))
num3 = float(input("Enter Third Angle Of Triangle:"))
if(num1 + num2 + num3 == 180):
    print("Valid Triangle.")
else:
    print("Not A Valid Triangle.")