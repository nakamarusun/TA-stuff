# Decorator
def check_zero(func):

    def finished(a, b):
        ## Checkings for 0
        if b == 0:
            return None
        return func(a, b)

    return finished

# Recommended way how to use decorator
@check_zero
def divide(a, b):
    return a / b

# Alternative way
def divide2(a, b):
    return a / b
new_divide = check_zero(divide2)

print(divide(5, 2))
print(divide(9, 0))
print(divide(2, 6))
print(divide(5, 9))
print(divide(7, 0))

print(new_divide(5, 1))