while(True):
    l = []
    add = 0
    a = int(input())
    if(a==(-1)):
        break
    for i in range(1,a+1):
        if(a%i==0):
            l.append(i)
    for i in range(len(l)-1):
        add = add+l[i]
    if(add==a):
        print(a,"=",end=" ")
        for i in range(len(l)-2):
            print(l[i],"+",end=" ")
        print(l[-2])
    else:
        print(a,"is NOT perfect.")