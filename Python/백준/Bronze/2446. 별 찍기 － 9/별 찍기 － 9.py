count = int(input())
for i in range(count,0,-1):
    for k in range(count-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()
for i in range(1,count):
    for j in range(count-1-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()