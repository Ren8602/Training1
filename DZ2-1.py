s = input()
flag = True
for i in s:
    if (i == 'a' or i == 'o'):
        flag == True
        continue

    elif i == 'i' or i == 'e':
        flag = False
        break
    
print(flag)