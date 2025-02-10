a = list(range(0,31))
answer = []
for i in range(28):
    num = int(input())
    a[num] = -1
for i in range(1,31):
    if(a[i]!=(-1)):
        answer.append(i)
print(min(answer))
print(max(answer))