
# Decorator


def decor(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        func(*args)
        print("After function execution")

    return wrapper


@decor
def sum(a, b):
    print(f"The sum is {a + b}")

sum(5,7)