k = int(input())
b =[]
i=0
try:
    while n:= input():
        i+=1
        a = n.split()
        spisok_int = list(map(int, a))
        if i<=k:
            maximum = max(spisok_int)
            b.append(maximum)
except:
    pass

b.sort(reverse=True)
result = ';'.join(str(i) for i in b)
print(result)