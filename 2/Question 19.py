marks1 = int(input("Enter Your Marks For Subject 1 And They Should Not Exceed 100: "))
marks2 = int(input("Enter Your Marks For Subject 2 And They Should Not Exceed 100: "))
marks3 = int(input("Enter Your Marks For Subject 3 And They Should Not Exceed 100: "))
marks4 = int(input("Enter Your Marks For Subject 4 And They Should Not Exceed 100: "))
marks5 = int(input("Enter Your Marks For Subject 5 And They Should Not Exceed 100: "))

if(marks1 > 100 or marks2 > 100 or marks3 > 100 or marks4 > 100 or marks5 > 100):
    print("You Have Entered Invalid Marks.")
else:
    average = (marks1+marks2+marks3+marks4+marks5)/5
    if((average >= 90) and (average <= 100)):
        print("Excellent!")
    elif((average >= 75) and (average < 90)):
        print("Very Good!")
    elif((average >= 60) and (average < 75)):
        print("Good!")
    elif((average >= 40) and (average < 60)):
        print("Average!")
    elif((average < 40) and (average >= 33)):
        print("Pass")
    else:
        print("Fail!")