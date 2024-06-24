my_input = input().lower()
my_set = set()
for s in my_input:
    if not s == ' ':
        my_set.add(s)
print(' '.join(sorted(my_set)))

