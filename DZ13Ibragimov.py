def transform(s):
    # a = list(map(str, s.split()))
    if s[0] == '!':
        s = s.upper()
    else:
        s = s.lower()
        
    for symb in '!@#%':
        s = s.replace(symb, '')   
    return s


b =[]
while s:=input():
    b.append(transform(s))

for i in b:
    print(i)