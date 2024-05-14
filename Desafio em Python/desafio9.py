import random

print("""--Gerador de Senhas Aleatórias--
    1 - Somente números
    2 - Números e letras
    3 - Números, letras e caracteres especiais\n""")

aux = True

while aux:
    tipo = int(input('Digite qual tipo de senha você deseja: '))

    if tipo == 1:
        aux = False
        caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        qtdCaracteres = int(input('Quantos caracteres você deseja: '))
        senha = ''

        while qtdCaracteres > 0:
            senha += caracteres[random.randint(0, len(caracteres) - 1)]
            qtdCaracteres -= 1
        
        print('Sua senha é:', senha)
    elif tipo == 2:
        aux = False
        caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        qtdCaracteres = int(input('Quantos caracteres você deseja: '))
        senha = ''

        while qtdCaracteres > 0:
            senha += caracteres[random.randint(0, len(caracteres) - 1)]
            qtdCaracteres -= 1
        
        print('Sua senha é:', senha)
    elif tipo == 3:
        aux = False
        caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' '!', '#', '$', '%', '&', '?', '@']

        qtdCaracteres = int(input('Quantos caracteres você deseja: '))
        senha = ''

        while qtdCaracteres > 0:
            senha += caracteres[random.randint(0, len(caracteres) - 1)]
            qtdCaracteres -= 1
        
        print('Sua senha é:', senha)
    else:
        print('Esta opção não existe.')