count = int(input())
for i in range(count):
    count2, word = input().split()
    count3 = 0
    for j in range(len(word)):
        for k in range(int(count2)):
            print(word[count3],end="")
        count3 = count3+1
    print()