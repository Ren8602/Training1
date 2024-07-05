lines=[]
while x:= input():
    if x[0]=='!':
        x=x.upper()
        lines.append(x)
    else:
        x=x.lower()
        lines.append(x)
def func(text):
    for char in ['!', '@', '#', '%']:
        text = text.replace(char, '')
    return text
# y = func(x)
for line in lines:
    print (func(line))