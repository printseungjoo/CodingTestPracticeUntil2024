import sys
input = sys.stdin.readline
count = int(input())
a = []
result = 0
for i in range(count):
    input2 = int(input())
    if(input2==0):
        if(len(a)==0):
            continue
        else:
            a.pop()
    else:
        a.append(input2)
for j in range(len(a)):
    result += a[j]
print(result)