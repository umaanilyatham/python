def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is running")
        result = func(*args, **kwargs)
        
        return result
    return wrapper
    

@my_decorator
def add(a, b):
    return a + b

print(add(10, 20))

@my_decorator
def sub(a, b):
    return a - b

print(sub(10, 20))

