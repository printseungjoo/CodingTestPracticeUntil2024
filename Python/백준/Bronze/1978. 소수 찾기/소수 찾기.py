count = int(input())
count2 = 0
num = list(map(int,input().split()))
for i in range(0,count):
    count3 = 0
    for j in range(1,num[i]+1):
        if(num[i]==1):
            continue
        if(num[i]%j==0):
            count3 = count3+1
    if(count3==2):
        count2 = count2+1
print(count2)