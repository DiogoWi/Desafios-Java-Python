print('---Calculadora Simples---\n')

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

print("""\n--Digite o número da operação---
  1 - Adição
  2 - Subtração
  3 - Multiplicação
  4 - Divisão""")

aux = True
while aux:
    operacao = int(input('Operação: '))

    if operacao == 1:
        resultado = numero1 + numero2
        aux = False
    elif operacao == 2:
        resultado = numero1 - numero2
        aux = False
    elif operacao == 3:
        resultado = numero1 * numero2
        aux = False
    elif operacao == 4:
        resultado = numero1 / numero2
        aux = False
    else:
        print('\nDigite uma das opções existentes.')

print('O resultado é:', resultado)