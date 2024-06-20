s = input()
dlina = 0
a = s.split()
for i in a:
    dlina += len(i)
print(dlina/len(a))
