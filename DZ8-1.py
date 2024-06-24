# cnt = abs(int(input()))
# data = list()
# try:
#     while meas := input():
#         data.append(meas)
# except:
#     pass
# ints = []
# for i in range(0, cnt, 1):
#     ints.append(max(list(map(int, data[i].split()))))
# print(';'.join(map(str,sorted(ints, reverse=True))))




cnt = abs(int(input()))
data = list()
n = 0
try:
    while meas := input():
        if n < cnt:
            data.append(max(list(map(int, meas.split()))))
            n += 1
except:
    pass
print(';'.join(map(str,sorted(data, reverse=True))))




# Необходимо написать программу, которая будет считывать последовательности измерений.
# В каждой последовательности нужно выбрать максимальное значение, а в итоге вывести отсортированный 
# по убыванию список этих макс значений, разделенных символом “;”. Во входных данных в первой строке будет
# задано целое положительное число – сколько записей нужно обработать, причем самих записей может быть больше
# чем это число, это нужно учесть. Значения в рамках одной записи разделены пробелом, минимальное число значений в записи – 1. 
# Записи разделены переводом строки.