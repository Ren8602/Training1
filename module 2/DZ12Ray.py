def average(nums_str):
    return sum(list(map(int, nums_str.split()))) / len(list(map(int, nums_str.split())))

while meas := input():
    print(average(meas))




# Чет этот код выбивает 1 из 4. Отдам свою клевую шариковую ручку тому кто решит на 4 из 4


# Необходимо написать программу, которая будет считывать со входа данные последовательностей чисел, 
# считать и выводить их среднее значение. Напишите сначала функцию, которая будет принимать строку, 
# а в ответ возвращать среднее значение чисел из нее. А далее применяйте эту функцию к каждой 
# считанной входной последовательности. На вход будут подаваться строки, в которых расположены целые числа, 
# разделенные пробелом. Передача пустой строки будет означать конец входных данных.