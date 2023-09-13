print("Variables")
print()
print("Type of Variables")
number = 10
money = 12.50
is_male = True
name = 'value'
no_value = None
print(type(number))
print(type(money))
print(type(is_male))
print(type(name))
print(type(no_value))
print()

print("Operations and Conversion")

print("Assignment Operations")
print('variable = "assignment"')
print("not will negate the boolean")
print("Arithmetic Operations")
print("+ - * / % // += -= *= /=")
print("Conditional Operations")
print("> < == != <= >= not is in ")

print("Conversions")
integer = 10
print(int(9.3))
print(float(9))
print(bool(0))
print(str(1))

one, two, three = 1, 2.0, "3"


def global_local():
    global one
    print(one)
    four = 4
    return


global_local()
# four -> this gives an error because it is a local variable of global_local function
