import sys
input = sys.stdin.readline
count = int(input())
a = []
b = []
for i in range(count):
    a = input().split()
    if(a[0]=="push"):
        b.append(a[1])
    elif(a[0]=="pop"):
        if(len(b)==0):
            print(-1)
        else:
            print(b.pop())
    elif(a[0]=="size"):
        print(len(b))
    elif(a[0]=="empty"):
        if(len(b)==0):
            print(1)
        else:
            print(0)
    else:
        if(len(b)==0):
            print(-1)
        else:
            print(b[-1])