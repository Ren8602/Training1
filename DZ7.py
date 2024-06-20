s = input()
dlina = 0
a = s.split()
for i in a:
    dlina += len(i)

if len(a) != 0:    
    print(dlina/len(a))
else:
    print(0)



