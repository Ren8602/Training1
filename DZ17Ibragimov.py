def map(func, seq):
   for i in seq:
      if func(i):
         yield i
func_in, seq_in = eval(input()), eval(input())
for x in map(func_in, seq_in):
   print(x)