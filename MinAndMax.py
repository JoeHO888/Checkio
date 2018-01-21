#Self-Written Max/Min function
#Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.
#Output: The largest item for the "max" function and the smallest for the "min" function.

def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    min_value = None
    for i in items:
        if min_value is None:
            min_value = i
        min_value = i if key(i) < key(min_value) else min_value
    return min_value

def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    max_value = None
    for i in items:
        if max_value is None:
            max_value = i
        max_value = i if key(i) > key(max_value) else max_value
    return max_value
