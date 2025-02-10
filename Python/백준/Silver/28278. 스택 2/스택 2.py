import sys
count = int(sys.stdin.readline())
stack = []
for i in range(count):
    input = list(map(int, sys.stdin.readline().split()))
    if(input[0]==1):
        stack.append(input[1])
    elif(input[0]==2):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack.pop())
    elif(input[0]==3):
        print(len(stack))
    elif(input[0]==4):
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    else:
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])