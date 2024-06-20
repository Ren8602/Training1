a = input()
count = 0

for i in a:
    if  (i == '!' or  i == '%' or i == '#' or i == '@') and i != ' ':
        a = a.replace(i, '')
        count = count + 1
print(count)   
print(a.lower())


# Код Рената
# a =(input())
# count = 0
# for i in a:
#   if i == '!' or  i == '%' or i == '#' or i == '@':
#     count +=1
# print (count)
# print(a.lower().replace("!", "").replace("#", "").replace("%", "").replace("@", ""))