count = int(input())
num = list(input())
answer = 0
for i in range(count):
    answer = answer+int(num[i:i+1][0])
print(answer)