a = []
for i in range(5):
    num = int(input())
    if(num<=40):
        a.append(40)
    else:
        a.append(num)
sum = 0
for i in range(5):
    sum+=a[i]
print(sum//5)