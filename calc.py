# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by 0!")
    return n1 / n2
