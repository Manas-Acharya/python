inp = list(map(float , input().split()))
x = inp[0]
y = inp[1]

if(x%5 == 0) and (y >= (x + .5)):
    b = y - (x+ .5)
    print("%.2f"%b)
else :
    print("%.2f"%y)
    
