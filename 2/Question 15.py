name = "sunny"
password = 1234
num1 = input("Enter User Name: ")
num = num1.lower()
code = int(input("Enter Password: "))
if(num == name and code == password):
    print("Access Granted!")
else:
    print("Access Denied!")