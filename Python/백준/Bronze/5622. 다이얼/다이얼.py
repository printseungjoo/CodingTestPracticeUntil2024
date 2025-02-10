word = input()
sum = 0
for i in range(len(word)):
    ac = ord(word[i])-65
    if(ac//3==0):
        sum+=3
    elif(ac//3==1):
        sum+=4
    elif(ac//3==2):
        sum+=5
    elif(ac//3==3):
        sum+=6
    elif(ac//3==4):
        sum+=7
    elif(ac==15 or ac==16 or ac==17 or ac==18):
        sum+=8
    elif(ac==19 or ac==20 or ac==21):
        sum+=9
    else:
        sum+=10
print(sum)