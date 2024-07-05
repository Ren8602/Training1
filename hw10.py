inv = input().lower()
words = inv.split()
wcount = {}
for word in words:
    if word in wcount:
        wcount[word]+=1
    else:
        wcount[word]=1
maxworld = max(wcount, key=wcount.get)
print(maxworld, wcount[maxworld])