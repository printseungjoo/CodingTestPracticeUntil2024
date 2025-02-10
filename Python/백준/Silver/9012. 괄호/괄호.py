import sys
count = int(sys.stdin.readline())
for i in range(count):
    tf = True
    stack = list()
    pList = list(sys.stdin.readline().strip())
    for j in range(len(pList)):
        if(pList[j]=='('):
            stack.append('(')
        else:
            if(len(stack)==0):
                print("NO")
                tf = False
                break
            else:
                stack.pop()
    if(len(stack)!=0 and tf!=False):
        print("NO")
        continue
    if(tf==True):
        print("YES")