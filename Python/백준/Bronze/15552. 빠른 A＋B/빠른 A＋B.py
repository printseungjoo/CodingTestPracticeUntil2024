import sys
count = int(sys.stdin.readline())
for i in range(count):
    num,num2 = map(int,sys.stdin.readline().split())
    print(num+num2)