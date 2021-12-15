'''summ=0
for x in range(2,201,2):
    summ = summ+x
    
    
    
print(summ)



summ=0
for x in range(1001,2000,2):
    print(x)
    summ = summ + x
print(summ)



n = int(input("Enter a number : "))
for i in range (1,n+1,2):
    print(i)
    '''

'''n=5
while(n>=0):
    r = int(input("Enter a number between 1 and 100 : "))
    if r>1 and r  <=100 :
        area = 3.14 * r**2
        print(area)
        break

    else:
        print('wrong number')
        if (n==1):
            print("Last chance")
        n -=1
   '''

n = int (input("Enter a number : "))
summ=2
for x in range (1,n+1):
         summ = (1/summ) + 1/(summ+2)
print(summ)
         
         
        



    
   
