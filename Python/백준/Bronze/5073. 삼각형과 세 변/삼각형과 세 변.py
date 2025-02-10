while(True):
    l = []
    bl = True
    a,a2,a3 = list(map(int,input().split()))
    if(a==a2==a3==0):
        break
    if(a>=a2 and a>=a3):
        if(a>=a2+a3):
            print("Invalid")
            bl = False
    elif(a2>=a and a2>=a3):
        if(a2>=a+a3):
            print("Invalid")
            bl = False
    else:
        if(a3>=a+a2):
            print("Invalid")
            bl = False
    if(bl==True):
        if(a==a2==a3):
            print("Equilateral")
        elif(a==a2 or a2==a3 or a3==a):
            print("Isosceles")
        else:
            print("Scalene")