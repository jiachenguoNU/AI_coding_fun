
#decorator should return the wrapper fun
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@my_decorator
def say_hello(*args, **kwargs):
    print(args)
    print("Hello!")
    print(kwargs)

say_hello(1,2,3, a=4,b=5)

@my_decorator
def say_(a,b):
    print("Hello!")
    print(a+b)
say_(1,2)


def add_to_class(Class):
    def wrapper(fun):
        setattr(Class, fun.__name__, fun)
    return wrapper

class ML_model():
    def __init__(self):
        self.inital_guess = 0 

@add_to_class(ML_model)
def print_init(self):
    print(f"initial guess is {self.inital_guess}")
A = ML_model()
A.print_init()