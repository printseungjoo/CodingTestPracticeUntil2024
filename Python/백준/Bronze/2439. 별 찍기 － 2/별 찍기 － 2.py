line = int(input())
blank = line-1
for i in range(line):
    for j in range(blank):
        print(" ", end="")
    for k in range(i+1):
        print("*",end="")
    print()
    blank=blank-1