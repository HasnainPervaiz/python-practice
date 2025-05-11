year = int(input("Enter A Year To Check If It Is A Leap Year: "))
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("This Is A Leap Year.")
else:
    print("This Is Not A Leap Year.")