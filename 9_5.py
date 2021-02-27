#Write a decorator that will output the execution time of a function

import time
def my_decorator(func):
    def wrapper(a, b):
        t = time.time()
        result = func(a, b)

        print(time.time() - t)
        return result
    return wrapper

@my_decorator
def foo(a=5, b=4):
    return (a + b)**(a+b)
print(foo(30, 44))