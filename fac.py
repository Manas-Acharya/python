num=int(input("Enter a number : "))

count=num
if (num==0):
    print(1)
elif (num<0):
    print("Enter a positive number ")
else    :
    while(count>1):
    
        count -=1
        num=num*count
    print(num)    
    

