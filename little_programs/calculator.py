def addition(a, b):
    add = a + b
    return add


def subtraction(a, b):
    sub = a - b
    return sub


def multiplication(a, b):
    multi = a*b
    return multi


def division(a, b):
    divi = a/b
    return divi


a = int(input('Insert the first number: '))
b = int(input('Insert the second number: '))

print() # Blank response
print() # Blank response

print('The sum between the values is: ', addition(a, b))
print('The difference between the values is: ', subtraction(a, b))
print('The multiplication between the number is: ', multiplication(a, b))
print('The division between the number is: ', division(a, b))