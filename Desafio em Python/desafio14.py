print('--Validador de Número de Cartão de Crédito--\n')

numero = input('Digite o número do cartão: ')[::-1]
digitosPares = 0
digitosImpares = 0

for i in range(1, len(numero) +  1):
    aux = 0

    if i % 2 == 0:
        aux = int(numero[i - 1]) * 2

        if aux > 9:
            digitosPares += aux - 9
        else:
            digitosPares += aux
    else:
        digitosImpares += int(numero[i - 1])

resultado = digitosPares + digitosImpares

if resultado % 10 == 0:
    print('Este cartão é valido.')
else:
    print('Este cartão é inválido.')