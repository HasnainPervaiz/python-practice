num1 = int(input("Enter A Number:"))
num2 = int(input("Enter A Number:"))
num3 = int(input("Enter A Number:"))
if(num1 > num2 and num1 > num3):
    print("Number 1 Is the Greatest And It Is: ",num1)
elif(num2 > num1 and num2 > num3):
    print("Number 2 Is the Greatest And It Is: ",num2)
elif(num3 > num2 and num3 > num1):
    print("Number 3 Is the Greatest And It Is: ",num3)