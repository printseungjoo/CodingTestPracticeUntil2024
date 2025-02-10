count = int(input())
for i in range(1,count+1):
    for j in range(count-i):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print()