n,m = map(int,input().split())
a,b,c = [],[],[]
for i in range(n):
    num = list(map(int,input().split()))
    a.append(num)
for j in range(n):
    num = list(map(int,input().split()))
    b.append(num)
for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j],end=" ")
    print()