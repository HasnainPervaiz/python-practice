time = float(input("Enter Your Time In Seconds: "))
hr = time/3600
min = time % 60
sec = min % 60
print("This time is equal to",hr ,"hour,",min,"minutes and",sec,"seconds.")