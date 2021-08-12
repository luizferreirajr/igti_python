peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura em metros: '))


def imc(peso, altura):
    imc_calc = peso/(altura**2)
    if imc_calc < 18.5:
        print('Magreza')
    elif 18.5 <= imc_calc <= 24.9:
        print('Normal')
    elif 25.0 <= imc_calc <= 29.9:
        print('Sobrepeso')
    elif 30.0 <= imc_calc <= 39.9:
        print('Obsedidade I')
    else:
        print('Obseidade II')
    return


print(imc(peso, altura))
