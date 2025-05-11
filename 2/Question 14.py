balance = int(input("Enter Total Balance: "))
if(balance <= 500):
    print("You Have Insufficient Balance.")
else:
    withdrawn = int(input("Enter Amount That You Want To Withdraw: "))
    if(withdrawn > balance):
        print("Withdrawal Should Not Exceed Balance.")
    elif(balance-withdrawn < 500):
        print("Insufficient Balance After Withdrawal.")
    elif(withdrawn % 100 == 0):
        print("Thankyou For Your Transaction.")