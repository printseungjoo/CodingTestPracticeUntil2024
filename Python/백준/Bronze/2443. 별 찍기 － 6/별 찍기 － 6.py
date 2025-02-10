count = int(input())
for i in range(count):
    for j in range(i):
        print(" ",end="")
    for k in range((count-i)*2-1):
        print("*",end="")
    print()