a = []
for i in range(5):
    ipt = list(input())
    a.append(ipt)
max = 1
for i in range(5):
    if(len(a[i])>=max):
        max = len(a[i])
sub = 0
for i in range(5):
    if(len(a[i])!=max):
        sub = max-len(a[i])
        for j in range(sub):
            a[i].append(-1)
        sub = 0
for i in range(max):
    for j in range(5):
        if(a[j][i]==(-1)):
            continue
        print(a[j][i],end="")
print()