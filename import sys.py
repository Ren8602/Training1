import sys
left = int(input('Введите левую границу'))
right = int(input())
count = 0
a = 0
n = sys.maxsize
for i in range(0, n):
    a = input()
    if a.isdigit():
        if int(a) not in range(left, right+1):
            count = count + 1
            break
    else:
        break
if count == 0:
    print('TRUE')
else:
    print('FALSE')