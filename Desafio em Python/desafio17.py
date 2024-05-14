print('--Fibonacci--\n')

quantidade = int(input('Digite quantos números da sequência Fibonacci você quer: '))
numeroAnterior = 0
numeroAtual = 1
aux = 0

for i in range(quantidade):
    print(numeroAtual)

    aux = numeroAtual
    numeroAtual += numeroAnterior
    numeroAnterior = aux