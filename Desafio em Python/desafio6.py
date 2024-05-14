print('--Cálculo de Média e Mediana--\n')

lista = []
media = 0
mediana = 0

for i in range(int(input('Digite quantos números irá ser inserido: '))):
    lista.append(int(input(f'Digite o {i+1}º número: ')))

for i in lista:
    media += i

if len(lista) % 2 == 0:
    meio = int(len(lista) / 2)
    mediana = (lista[meio - 1] + lista[meio]) / 2
else:
    meio = int(len(lista) / 2)
    mediana = lista[meio]

print('A média dos números digitados é:', media / len(lista))
print('A mediana da lista de números é:', mediana)