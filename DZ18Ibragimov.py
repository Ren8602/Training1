def cache_deco(func):
    cache = {}
    def wrapper(k):
        if k in cache:
            return cache[k]
        result = func(k)
        cache[k] = result
        return result
    return wrapper
   
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code) 

# @cache_deco
# def fib(k):
#     if k <= 2:
#         return 1
#     return fib(k - 1) + fib(k - 2)
# print(fib(10))




