a,a2 = map(int,input().split())
b,b2 = map(int,input().split())
c,c2 = map(int,input().split())
if(a==b):
    if(c2==a2):
        print(c,b2)
    else:
        print(c,a2)
elif(a==c):
    if(b2==a2):
        print(b,c2)
    else:
        print(b,a2)
else:
    if(a2==b2):
        print(a,c2)
    else:
        print(a,b2)