age = int(input("Enter Your Age To Check Voting Eligibility: "))
if(age >= 18):
    print("Eligible To Vote.")
elif(age < 18 and age > 0):
    print("Not Eligible To Vote.")
else:
    print("Age Should Be Greater Than 0.")