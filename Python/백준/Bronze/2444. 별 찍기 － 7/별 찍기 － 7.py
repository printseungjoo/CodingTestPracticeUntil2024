count = int(input())
blank = count-1
star = 1
for i in range(count-1):
    for k in range(blank):
        print(" ",end="")
    for m in range(star):
        print("*",end="")
    blank = blank-1
    star = star+2
    print()
for i in range(count*2-1):
    print("*",end="")
print()
blank = blank+1
star = star-2
for i in range(count-1):
    for k in range(blank):
        print(" ",end="")
    for m in range(star):
        print("*",end="")
    blank = blank+1
    star = star-2
    print()