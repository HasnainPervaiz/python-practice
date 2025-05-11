num = float(input("Enter Obtained Marks: "))
if(num >= 90):
    print("Grade = A")
elif(num < 90 and num >= 80):
    print("Grade = B")
elif(num < 80 and num >= 70):
    print("Grade = C")
else:
    print("Grade = D")