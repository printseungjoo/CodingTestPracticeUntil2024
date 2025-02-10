count = int(input())
a = list(map(int,input().split()))
score = max(a)
answer = 0
for i in range(len(a)):
    answer = answer+a[i]/score*100
print(answer/len(a))