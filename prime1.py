num=int(input("Enter a number "))
for i in range(2,num**0.5):
    if num%i==0 :
        print("Not prime")
        break
else :
    print("Prime")
