import pandas as pd
import numpy as np

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

"""#a. Qual o tamanho desse dataset?
print('A')
print(len(df))
"""

"""#b. Qual a média da coluna windspeed?
print('B')
print(df['windspeed'].mean())
"""

"""#c. Qual a média da coluna temp?
print('C')
print(df['temp'].mean())
"""

"""#d. Quantos registros existem para o ano de 2011?
print('D')
print(len(df[df['year'] == 0]))
"""

"""#e. Quantos registros existem para o ano de 2012?
print('E')
print(len(df[df['year'] == 1]))
"""

"""#f. Quantas locações de bicicletas foram efetuadas em 2011?
#year: ano (0: 2011, 1:2012);

print('F')
cond = df[df['year'] == 0]

print(cond['total_count'].sum())
"""

"""#g. Quantas locações de bicicletas foram efetuadas em 2012?
print('G')
cond = df[df['year'] == 1]

print(cond['total_count'].sum())
"""

"""#h. Qual estação do ano contém a maior média de locações de bicicletas?
#season: estação do ano (1: inverno, 2: primavera, 3: verão, 4: outono).
print('H')

df = df.set_index('season')

print(df.groupby('season').mean()['total_count'])
"""

"""#j. Qual horário do dia contém a maior média de locações de bicicletas?
print('J')

df = df.set_index('hour')

print(df.groupby('hour').mean()['total_count'].max())
print(df.groupby('hour').mean()['total_count'])
"""

"""#l. Que dia da semana contém a maior média de locações de bicicletas?
print('L')

df = df.set_index('weekday')

print(df.groupby('weekday').mean()['total_count'])
"""

"""#n. Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média
#de locações de bicicletas?
print('N')

df = df.set_index('hour')

cond = df[df['weekday'] == 3]


print(cond.groupby('hour').mean()['total_count'].max())
print(cond.groupby('hour').mean()['total_count'])
"""

#Aos sábados (weekday = 6), qual o horário do dia contém a maior média de
#locações de bicicletas?
print('O')

df = df.set_index('hour')

cond = df[df['weekday'] == 6]


print(cond.groupby('hour').mean()['total_count'].max())
print(cond.groupby('hour').mean()['total_count'])
