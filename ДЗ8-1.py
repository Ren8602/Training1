cnt = abs(int(input()))
data = list()
while meas := input():
    data.append(meas)

ints = ''
for i in range(0, cnt, 1):
    ints = ints + str(max(list(map(int, data[i].split()))))
    # Эта хрень чтобы не добавлять в конец точку с запятой:
    if not i == cnt-1:
        ints += ';'
print(ints)
     


# ТОЖЕ ВЫДАЕТ ОШИБКУ RE. хмм...





# Необходимо написать программу, которая будет считывать последовательности измерений.
# В каждой последовательности нужно выбрать максимальное значение, а в итоге вывести отсортированный 
# по убыванию список этих макс значений, разделенных символом “;”. Во входных данных в первой строке будет
# задано целое положительное число – сколько записей нужно обработать, причем самих записей может быть больше
# чем это число, это нужно учесть. Значения в рамках одной записи разделены пробелом, минимальное число значений в записи – 1. 
# Записи разделены переводом строки.