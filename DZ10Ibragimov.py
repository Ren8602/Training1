s = input().lower()
dlina = 0
word_count = 0
max = 0
a = s.split()

for i in a:
    word_count = 0
    for j in a:
        if i == j:
            word_count +=1
    if word_count > max:
        max = word_count
        word = i

print(word, max)