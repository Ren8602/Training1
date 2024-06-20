word = input()
count = 0
rep = '!%#@'
for l in rep:
    if l in word:
        count +=1
    word = word.replace(l,'')
print(count)
print(word.lower())


