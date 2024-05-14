def primo(numero):
    if numero <= 1:
        print(numero, 'não é primo')
    else:
        for i in range(2, numero):
            if numero % i == 0:
                print(numero, 'não é primo')
                break
        else:
            print(numero, 'é primo')

print('--Verificador de Número Primo--\n')

numero = int(input('Digite um número: '))

primo(numero)
