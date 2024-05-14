print('--Verificador de Palíndromo--\n')

palavra = input('Digite uma palavra: ')

if palavra.replace(' ', '').lower() == palavra[::-1].replace(' ', '').lower():
    print('\nEssa palavra é um palíndromo:')
    print(palavra) 
    print(palavra[::-1])
else:
    print('\nEssa palavra não é um palíndromo.')