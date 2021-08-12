num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Aprendendo sobre def e lambda

"""
def soma(x, y):
    subtotal = x + y
    return subtotal


print(soma(num1, num2))
"""


soma = lambda x, y: x + y
print(soma(num1, num2))

