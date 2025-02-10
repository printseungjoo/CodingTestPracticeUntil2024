count, num = map(int,input().split())
a = list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]<num):
        print(a[i],end=' ')
print()