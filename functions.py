print("Functions")


def add(value1, value2):
    return value1 + value2


def subtract_one(value):
    return value - 1


def add_value(value, amount=1):
    return value + amount


def addition(*values):
    return sum(values[0])

def key_values(**kwargs):
    print(kwargs.items())

def pass_function():
    pass

print(addition([1, 2, 3, 4]))
key_values(Dileep=2, Shushanth=4)