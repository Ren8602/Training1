s = input().lower()
count = 0
k = 0 
symb = '!,.?;:#$%^&*()'

for i in s:
    if i in symb:
        s = s.replace(i, '')

a = s.split()
b = []
for i in a:
    k = 0
    if len(i) >= 5 and len(set(i)) >= 4 and a.count(i) > 2:
        b.append(i)

result = sorted(list(set(b)))
for i in result:
    print(i)



