import sys
num = int(sys.stdin.readline())
a = []
while(num!=0):
    a.append(num%10)
    num//=10
a = sorted(a,reverse=True)
for i in range(len(a)):
    print(a[i],end="")
print()