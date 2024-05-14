def fatorial(numero):
    for i in range(2, numero):
        numero *= i
    print('O fatorial é:', numero)

print('--Fatorial de um Número--')
numero = int(input('Digite um número: '))
fatorial(numero)