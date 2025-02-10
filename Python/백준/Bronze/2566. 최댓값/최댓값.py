a = []
for i in range(9):
    num = list(map(int,input().split()))
    a.append(num)
max = 0
maxIndex = 1
maxIndex2 = 1
for i in range(9):
    for j in range(9):
        if(a[i][j]>=max):
            max = a[i][j]
            maxIndex = i+1
            maxIndex2 = j+1
print(max)
print(maxIndex, maxIndex2)