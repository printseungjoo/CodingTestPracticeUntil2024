a,b = map(int,input().split())
l = []
for i in range(1,a+1):
    if(a%i==0):
        l.append(i)
if(len(l)==0 or len(l)<b):
    print(0)
else:
    print(l[b-1])