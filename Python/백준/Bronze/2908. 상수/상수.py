num1, num2 = map(int,input().split())
hun = num1//100
mid = num1%100//10
one = num1%10
num1 = one*100+mid*10+hun
hun = num2//100
mid = num2%100//10
one = num2%10
num2 = one*100+mid*10+hun
if(num1>=num2):
    print(num1)
else:
    print(num2)