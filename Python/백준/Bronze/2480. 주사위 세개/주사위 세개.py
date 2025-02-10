a,b,c=map(int,input().split())
if(a==b==c):
    print(10000+a*1000)
elif(a==b or b==c):
    print(1000+b*100)
elif(c==a):
    print(1000+c*100)
else:
    if(a>=b and a>=c):
        big = a
    elif(b>=a and b>=c):
        big = b
    else:
        big = c
    print(big*100)