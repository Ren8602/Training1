inv = input()
for smv in '!,.?;:#$%^&*(),':
    inv = inv.replace(smv, '')
words = inv.split()
words.sort()
filter_words = []
wcount = []
a = []
for word in words:
    if words.count(word) > 2 and len(word)>=5 and len(set(word))==4:
        wcount.append(word)
print (wcount)
# for word in wcount:
#     if len(word)>=5:
#         filter_words.append(word)
# for word in filter_words:
#     if len(set(word))==4:
#         a.append(word)
# print(a)
# Необходимо написать программу, которая будет принимать на вход строку, 
# разбивать строку на слова по пробелу. 
# Далее нужно из всех слов убрать следующие пунктуационные знаки: 
# а также привести слова к нижнему регистру. 
# В итоге нужно вывести в алфавитном порядке слова, которые состоят как минимум из 5 символов,
# а также имеют как минимум 4 уникальных символа,
# и которые встретились в исходном тексте более 2х раз.