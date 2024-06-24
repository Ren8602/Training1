sentense = input().lower()
words = sentense.split()
for word in words:
    if words.count(word) > 1:
        print(word + ' ' +  str(words.count(word)))
        break