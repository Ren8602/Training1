izm = abs(int(input()))
b = []
try:
    while a:= input():
        b.append(a)
except:
    pass
out = []
for i in range (0, izm, 1):
    out.append(max(list(map(int, b[i].split()))))
print(';'.join(map(str,sorted(out, reverse=True))))