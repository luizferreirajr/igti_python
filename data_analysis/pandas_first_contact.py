import pandas as pd

# leitura de arquivo csv
# df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
# print(df)

# leitura de planilhas excel
# 2 abas (worksheets)

# leitura do arquivo completo
excel_file = pd.ExcelFile('https://pycourse.s3.amazonaws.com/temperature.xlsx')
# print(excel_file)


# leitura da primeira aba (Sheet 1)
# dados numéricos com separador decimal = '.'
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print(df2)

# leitura da primeira aba (Sheet 2)
# dados numéricos com separador decimal = ','
df3 = pd.read_excel(excel_file, sheet_name='Sheet2')
print(df3)

# visualizando as 3 primeiras linhas
n = 3
print(df2.head(n))

# estatísticas básicas
print(df2.describe())

# dataframe info
print(df2.info)

# dataframe columns
print(df2.columns)