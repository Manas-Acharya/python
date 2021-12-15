import random

c=input("Enter your choice Rock[R],Paper[P],Scissors[S] : ")
choices=('R','S','P')
ComputerChoice = random.choice(choices)

if c==ComputerChoice :
     print("Your choice :",c)
     print("Computer's choice :",ComputerChoice)
     print("Tie")
     
   
elif c=='R' and ComputerChoice=='P' :
     print("Your choice : Rock",c)
     print("Computer's choice : Paper ")
     print("Computer Wins")
     
elif c=='R' and ComputerChoice=='S' :
     print("Your choice : Rock")
     print("Computer's choice : Scissors ")
     print("YOU WIN")
     
elif c=='P' and ComputerChoice=='S' :
     print("Your choice : Paper ")
     print("Computer's choice : Scissors ")
     print("Computer Wins")
     
elif c=='P' and ComputerChoice=='R' :
     print("Your choise : Paper")
     print("Computer's choice : Rock :")
     print("YOU WIN")
     
elif c=='S' and ComputerChoice=='R' :
     print("Your choice : Scissors")
     print("Computer's choice : Rock")
     print("Computer Wins")
     
elif c=='S' and ComputerChoice=='P' :
     print("Your choice : Scissors")
     print("Computer's choice : Paper")
     print("YOU WIN")     

else :
    print("Invalid Input. Try again with [R], [P] or [S] ")
    
