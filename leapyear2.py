Y=int(input("Enter the year : "))

if Y%4==0 and Y%100!=0 :
    
       print(Y,"is a leap year")
else :
    if Y%400==0:
        print(Y,"is a leap year")

    else :
        print(Y,"is not a leap year")
