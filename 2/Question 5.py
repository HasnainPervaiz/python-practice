num = int(input("Enter A Number To Check If It Is Divisible By Both 5 And 11: "))
if(num % 5 == 0 and num % 11 == 0):
    print("The Number Is Divisible By Both 5 And 11.")
elif(num % 5 != 0 and num % 11 == 0):
    print("The Number Is Divisible By 11 But Not By 5.")
elif(num % 5 == 0 and num % 11 != 0):
    print("The Number Is Divisible By 5 But Not By 11.")
else:
    print("The Number Is Not Divisible By Both 5 And 11.")