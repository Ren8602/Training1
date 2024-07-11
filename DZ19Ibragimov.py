def repeat_deco(n=1):
   def my_decorator(func):
      def wrapper(*args, **kwargs):
         for i in range(n):
            result = func(*args, **kwargs)
         return result
      return wrapper
   return my_decorator


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# @repeat_deco(4)
# def hello():
#     print("hello")
# hello()



# def conditional_decorator(condition):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if condition:
#                 return f"Function {func.__name__} is disabled"
#             else:
#                 return func(*args, **kwargs)
#         return wrapper
#     return decorator

# @conditional_decorator(condition=True)
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))
