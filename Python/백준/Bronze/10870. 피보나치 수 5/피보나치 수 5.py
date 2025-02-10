def f(num):
    if num<=1:
        return num
    else:
        return f(num-1)+f(num-2)

num = int(input())
print(f(num))