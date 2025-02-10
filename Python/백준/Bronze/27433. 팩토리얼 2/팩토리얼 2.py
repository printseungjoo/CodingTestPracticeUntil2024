num = int(input())
ans = 1
for i in range(num+1):
    if(i==0):
        continue
    else:
        ans*=i
print(ans)