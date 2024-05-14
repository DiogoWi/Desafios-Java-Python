import os

print('--Jogo da Forca--')

palavra = []
palavraOculta = []
chances = 6
aux = True

for i in input('Escolha uma palavra para ser adivinhada: '):
    palavra.append(i)
    palavraOculta.append('_')

os.system('cls')
print(palavraOculta)

while aux:
    acerto = 0

    print('\nVocê tem', chances, 'chances de errar.')
    letra = input('Escolha uma letra: ')

    for i in range(len(palavra)):
        if palavra[i] == letra:
            acerto += 1
            palavraOculta[i] = letra
        
    if acerto == 0:
        chances -= 1

    print(palavraOculta)

    for i in palavraOculta:
        if chances == 0:
            aux = False
            print('Suas chances acabaram.')
            break
        elif i == '_':
            aux = True
            break
        else:
            aux = False
    else:
        print('Parabéns você ganhou.')