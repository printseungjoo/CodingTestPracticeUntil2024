n,m = map(int,input().split())
a = []
for i in range(n+1):
    a.append(0)
for i in range(m):
    range1,range2,num = map(int,input().split())
    for j in range(range1,range2+1):
        a[j] = num
for i in range(1,n+1):
    print(a[i], end = " ")
print()