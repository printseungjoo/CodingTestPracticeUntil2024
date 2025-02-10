a = list()
for i in range(42):
    a.append(0)
for i in range(10):
    num = int(input())
    a[num%42] = a[num%42]+1
count = 0
for i in range(42):
    if(a[i]!=0):
        count = count+1
print(count)