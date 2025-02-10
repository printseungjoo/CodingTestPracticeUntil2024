import sys
student = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
count = 0
for i in range(len(a)):
    if(a[i]==0):
        continue
    elif(a[i]<=b[0]):
        count+=1
    elif(a[i]%b[0]==0):
        count+=a[i]//b[0]
    else:
        count+=a[i]//b[0]+1
print(count)
count2 = student//b[1]
count3 = student-count2*b[1]
print(count2,count3)