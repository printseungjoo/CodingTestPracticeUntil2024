import sys
count = int(sys.stdin.readline())
mul = 1
for i in range(2,count+1):
    mul*=i
a = list(str(mul))
answer = 0
for i in range(len(a)):
    if(a[len(a)-1-i]=='0'):
        answer+=1
    else:
        break
print(answer)