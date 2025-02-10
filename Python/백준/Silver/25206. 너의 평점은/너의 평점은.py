gpa = 0
gpa2 = 0
count = 0
for i in range(20):
    subject,gpa3,gpa4 = input().split()
    if(gpa4=="A+"):
        gpa2 = 4.5
    elif(gpa4=="A0"):
        gpa2 = 4.0
    elif(gpa4=="B+"):
        gpa2 = 3.5
    elif(gpa4=="B0"):
        gpa2 = 3.0
    elif(gpa4=="C+"):
        gpa2 = 2.5
    elif(gpa4=="C0"):
        gpa2 = 2.0
    elif(gpa4=="D+"):
        gpa2 = 1.5
    elif(gpa4=="D0"):
        gpa2 = 1.0
    elif(gpa4=="F"):
        gpa2 = 0.0
    else:
        continue
    gpa = gpa+float(gpa3)*gpa2
    count = count+float(gpa3)
print(gpa/count)