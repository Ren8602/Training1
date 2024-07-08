








def cache_deco(func):
   

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code) 



# Входные данные

# @cache_deco
# def fib(k):
#     if k <= 2:
#         return 1
#     return fib(k - 1) + fib(k - 2)
# print(fib(30))


# Напишите декоратор, который будет кэшировать вызовы функции, которая будет передана на вход.
# То есть декоратор должен проверить нет ли в кэше (например, словаре) значения, и если нет,
# то вычислить и запомнить результат, если есть, то взять это значение. Дополните код ниже, 
# дописав свой код в секции “YOUR CODE HERE”.





# def my_decorator(func):
#     print('before wrapper')

#     def wrapper():
#         print('before func call')
#         func()
#         print('after func call')

#     print('after wrapper')
#     return wrapper


# @my_decorator
# def my_func():
#     print('My func printed this')


# #my_decorated_func = my_decorator(my_func)
# my_func()