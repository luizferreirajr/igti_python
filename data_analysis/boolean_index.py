import numpy as np

# Criação de arrays

x = np.array([[1, 2], [3, 4]])
y = np.array([[1.5, 3.5]])
print('x: \n', x)
print('y: \n', y)

# Comparações ponto a ponto
print('Comparação de um array com um escalar (>): \n', x > 2)
print('Comparação de um array com um escalar (>=): \n', x >= 2)
print('Comparação de um array com um escalar (<): \n', x < 2)
print('Comparação de um array com um escalar (<=): \n', x <= 2)
print('Comparação entre arrays (==): \n', x == x)
print('Comparação entre arrays (>): \n', x > x)
print('Comparação entre arrays (<): \n', x < y) # broadcasting

print()


print('Segunda atividade: Indexação booleana\n'
      'Retornar o número de elementos maiores que k')

# indexação booleana
a = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])
print('a: \n', a)

k = 10
cond = a > k
print('condição: \n', cond)
print('elementos maiores que {k}: ', a[cond])
print('número de elementos maiores que {k}:', len(a[cond]))

# indexação booleana: extração de números pares
cond2 = a % 2 == 0  # números pares
print('condição: \n', cond2)
print('números pares:', a[cond2])

# indexação booleana: extração de números ímpares
cond2 = a % 2 != 0  # números pares
print('condição: \n', cond2)
print('números ímpares:', a[cond2])

