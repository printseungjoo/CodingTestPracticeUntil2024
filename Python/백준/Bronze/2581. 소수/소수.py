num = int(input())
num2 = int(input())
l = []
for i in range(num,(num2)+1):
    count = 0
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                count+=1
                break
        if(count==0):
            l.append(i)
if(len(l)>0):
    print(sum(l))
    print(min(l))
else:
    print(-1)