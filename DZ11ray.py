text = input().lower()
for symb in '!,.?;:#$%^&*()': # Удалим эти символы из текста
    text = text.replace(symb, '')

list_of_words = text.split() # Промежуточноая переменная. Получим список из всех слов текста. Оказалось, если перебирать список и в нем же удалять сразу элементы то цикл перепрыгивает и не все удаляет.

for word in text.split(): # Удалим слова, которые не удовлетворяют требованию по общему количеству символов, количеству уникальных символов и количеству повторений в тексте
    if len(word) < 5 or len(set(word)) < 4 or text.split().count(word) <= 2:
       list_of_words.remove(word)

result = sorted(list(set(list_of_words))) # Set оказался крут. Можно пихать список но добавятся только уникальные элементы. Преобразуем его опять в список и его уже отсортируем - оказывается сортировать напрямую set нельзя.

for r in result: # Коварная херная, изза которой не приняли сначала. Оказывается каждое слово нужно печатать отдельно...
    print(r)