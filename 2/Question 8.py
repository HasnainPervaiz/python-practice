num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
if(num1 > num2 and num1 > num3):
    print("Number 1 Is The Greatest")
elif(num2 > num1 and num2 > num3):
    print("Number 2 Is The Greatest")
elif(num3 > num1 and num3 > num2):
    print("Number 3 Is The Greatest")
else:
    print("All Numbers Are Equal.")