num,count = map(int,input().split())
a = [0]*(num+1)
for i in range(num+1):
    a[i] = i
for i in range(count):
    idx,idx2 = map(int,input().split())
    minus = idx2-idx
    count2 = minus//2+1
    for j in range(count2):
        temp = a[idx]
        a[idx] = a[idx2]
        a[idx2] = temp
        idx = idx+1
        idx2 = idx2-1
for i in range(1,len(a)):
    print(a[i],end=" ")
print()