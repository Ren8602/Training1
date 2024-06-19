s = input()
flag = True
for i in s:
    if (i == 'a' or i == 'o'):
        flag == True
        continue

    elif i == 'i':
        flag = False
        break

    elif i == 'e':
        flag = False
        break


print(flag)