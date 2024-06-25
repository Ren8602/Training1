inv = input()
for smv in '!,.?;:#$%^&*(),':
    inv = inv.replace(smv, '')
words = inv.split()
words.sort()
filter_words = []
wcount = {}
for word in words:
    if word in words:
        wcount[word]+=1
    else:
        wcount[word] = 1
    if wcount[word] > 2:
        filter_words.append(word)
    if len(word)>=5:
        filter_words.append(word)

print(filter_words)
# Необходимо написать программу, которая будет принимать на вход строку, 
# разбивать строку на слова по пробелу. 
# Далее нужно из всех слов убрать следующие пунктуационные знаки: 
# а также привести слова к нижнему регистру. 
# В итоге нужно вывести в алфавитном порядке слова, которые состоят как минимум из 5 символов,
# а также имеют как минимум 4 уникальных символа,
# и которые встретились в исходном тексте более 2х раз.