units = int(input("Enter The Number Of Units Consumed: "))
if((units - 100) <= 0):
    bill = 0
else:
    if((units - 100) < 100):
        bill = units*5
    else:
        units = units - 100
        extraUnits = units - 100
        extraUnits = extraUnits * 10
        bill = 500 + extraUnits

print("your bill is: ",bill) 