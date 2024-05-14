def maiorNumero(lista):
    maior = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    
    print(f'O maior número desta lista é: {maior}')

def menorNumero(lista):
    menor = lista[0]

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    
    print(f'O menor número desta lista é: {menor}')

print('--Encontrar o Maior e o Menor Número em uma Lista--\n')

lista = input('Digite uma lista de números: ')
lista = lista.split(' ')
for i in range(len(lista)):
    lista[i] = int(lista[i])

maiorNumero(lista)
menorNumero(lista)