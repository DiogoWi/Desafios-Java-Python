print('--Ordenação de Listas--\n')

lista = []
quantidade = int(input('Digite quantos números terá na lista: '))

while quantidade > 0:
    lista.append(int(input('Digite o número: ')))
    quantidade -= 1

for i in range(len(lista) -1):
    for j in range(len(lista) -1):
        if (lista[j] > lista[j + 1]):
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print('\nAqui está sua lista ordenada:', lista)