num = int(input())
a = list()
count = 2
while(num!=1):
    if(num%count==0):
        print(count)
        num = num//count
    else:
        count = count+1