n,m = map(int,input().split())
a = list(range(n+1))
for i in range(m):
    switch1, switch2 = map(int,input().split())
    temp = a[switch1]
    a[switch1] = a[switch2]
    a[switch2] = temp
for i in range(1,n+1):
    print(a[i], end=" ")
print()