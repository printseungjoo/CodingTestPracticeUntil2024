num = int(input())
b = True
if(num%4==0):
    if(num%100!=0):
        print("1")
        b = False
if(num%400==0):
    print("1")
    b = False
if(b==True):
    print("0")