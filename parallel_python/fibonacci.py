

def fibonacci(n):
    """Calculate a fibonacci value from the given n"""
    a, b = 0, 1
    for item in range(n):
        a, b = b, a + b

    return a


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


for i in range(1, 11):
    print(fibonacci(i))