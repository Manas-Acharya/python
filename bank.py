withdrawAmount=float(input("Enter the amount to withdraw : "))
bankBalance=20000

if withdrawAmount%5==0 and bankBalance>withdrawAmount+.5 :
    print("Transaction Successfull ")
    bankBalance-=(withdrawAmount)+.5
    print("Bank balance after withdrawl = ",bankBalance)

else :
    print("Transaction Failed")
