word = input()
count = 0
for i in range(len(word)//2):
    if(word[i]==word[len(word)-1-i]):
        count = count+1
if((len(word)//2)==count):
    print("1")
else:
    print("0")