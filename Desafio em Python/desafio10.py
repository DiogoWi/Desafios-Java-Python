import random

print('--Simulador de Dados--\n')

dados = int(input('Quantos dados serão lançados: '))
soma = 0
i = 0

while dados > 0:
    i += 1
    dados -= 1

    resultado = random.randint(1, 6)
    soma += resultado
    print(f'{i}° dado: {resultado}')

print('A soma dos dados é:', soma)