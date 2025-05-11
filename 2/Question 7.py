char = input("Enter A Character: ")
if(char.isupper()):
    print("Uppercase Letter.")
elif(char.islower()):
    print("Lowercase Letter.")
elif(char.isdigit()):
    print("Digit.")
else:
    print("Special Character.")
