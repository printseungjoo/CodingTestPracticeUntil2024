alpha = [-1]*26
word = input()
for i in range(len(word)):
    idx = ord(word[i])-97
    if(alpha[idx]!=(-1)):
        continue
    else:
        alpha[idx] = i
for i in range(len(alpha)):
    print(alpha[i],end=" ")
print()