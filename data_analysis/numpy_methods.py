import numpy as np

# array
x = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])
print('x: \n', x)

# reshape: transformar a matriz em um vetor coluna
# (3, 3) vira (9, 1): 3*3 = 9*1 = 9
# print('Transformação em um vetor coluna: \n', x.reshape(9, 1))

# transposição de matriz
# print('x transposta: \n', x.T)

# np.sum: soma em um dado eixo, axis = {0: linha, 1: coluna}
print('soma de todos os elementos de x: ', np.sum(x))
print('soma de x ao longo das linhas: ', np.sum(x, axis=0))
print('soma de x ao longo das colunas: ', np.sum(x, axis=1))
print()

# np.mean: média em um dado eixo, axis = {0: linha, 1: coluna}
print('media de todos os elementos de x: ', np.mean(x))
print('media de x ao longo das linhas: ', np.mean(x, axis=0))
print('media de x ao longo das colunas: ', np.mean(x, axis=1))
print()

# np.where, identificação dos índices onde uma dada condição
# é atendida. Uso conjunto com indexação booleana
# cond = x % 2 == 0  # números pares
# print('condição: \n', cond)
# i, j = np.where(cond)  # indices x[i, j] = x[cond]
# print('índice i (linhas): ', i)
# print('índice j (linhas): ', j)

# indexação booleana e slicing: selecionar as linhas
# de x que possuem algum número par
cond = x % 2 == 0 #  números pares
print('condição: \n', cond)

# se houver alguma condição True na linha, a soma será > 0
i_row = np.where(np.sum(cond, axis=1))[0]
print('índice das linhas que possuem números pares: ', i_row)
print('linhas que possuem números pares: \n', x[i_row, :])
