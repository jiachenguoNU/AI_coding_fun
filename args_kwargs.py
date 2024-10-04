def print_all_arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
'''
Single Asterisk (*args)
When used in function definitions, the single asterisk * is followed by a parameter name (commonly args), and it allows the function to accept an arbitrary number of positional arguments. These arguments are then accessible within the function as a tuple.

Usage: *args is typically used when you want to allow a function to take any number of positional arguments.

Behavior: The function collects all the positional arguments passed to it and packs them into a tuple.


Double Asterisk (**kwargs)
When you use a double asterisk ** in function definitions, it is followed by a parameter name (commonly kwargs), and it allows the function to accept an arbitrary number of keyword arguments. These arguments are accessible within the function as a dictionary.

Usage: **kwargs is used to handle keyword arguments, where arguments are passed in the form key=value.

Behavior: The function collects all the keyword arguments passed to it and packs them into a dictionary.


'''
print_all_arguments(1, 2, a=3, b=4)
# Output:
# Positional arguments: (1, 2) -> becomes a tuple
# Keyword arguments: {'a': 3, 'b': 4} -> becomes a dict