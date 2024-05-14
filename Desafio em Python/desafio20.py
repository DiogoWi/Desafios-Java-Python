def imprimirJogo():
    print('\n     1º  2º  3º')
    for i in range(len(jogo)):
        print(f'{i + 1}º {jogo[i]}')

def ganhou(jogo):
    # Linhas
    if jogo[0][0] == 'X' and jogo[0][1] == 'X' and jogo[0][2] == 'X':
        # Linha 1
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[0][0] == 'O' and jogo[0][1] == 'O' and jogo[0][2] == 'O':
        # Linha 1
        print('O jogador 2 ganhou!!!')
        exit()
    elif jogo[1][0] == 'X' and jogo[1][1] == 'X' and jogo[1][2] == 'X':
        # Linha 2
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[1][0] == 'O' and jogo[1][1] == 'O' and jogo[1][2] == 'O':
        # Linha 2
        print('O jogador 2 ganhou!!!')
        exit()
    elif jogo[2][0] == 'X' and jogo[2][1] == 'X' and jogo[2][2] == 'X':
        # Linha 3
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[2][0] == 'O' and jogo[2][1] == 'O' and jogo[2][2] == 'O':
        # Linha 3
        print('O jogador 2 ganhou!!!')
        exit()
    # Colunas
    elif jogo[0][0] == 'X' and jogo[1][0] == 'X' and jogo[2][0] == 'X':
        # Coluna 1
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[0][0] == 'O' and jogo[1][0] == 'O' and jogo[2][0] == 'O':
        # Coluna 1
        print('O jogador 2 ganhou!!!')
        exit()
    elif jogo[0][1] == 'X' and jogo[1][1] == 'X' and jogo[2][1] == 'X':
        # Coluna 2
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[0][1] == 'O' and jogo[1][1] == 'O' and jogo[2][1] == 'O':
        # Coluna 2
        print('O jogador 2 ganhou!!!')
        exit()
    elif jogo[0][2] == 'X' and jogo[1][2] == 'X' and jogo[2][2] == 'X':
        # Coluna 3
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[0][2] == 'O' and jogo[1][2] == 'O' and jogo[2][2] == 'O':
        # Coluna 3
        print('O jogador 2 ganhou!!!')
        exit()
    # Diagonais
    elif jogo[0][0] == 'X' and jogo[1][1] == 'X' and jogo[2][2] == 'X':
        # Esquerda para direita
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[0][2] == 'X' and jogo[1][1] == 'X' and jogo[2][0] == 'X':
        # Direita para esquerda
        print('O jogador 1 ganhou!!!')
        exit()
    elif jogo[0][0] == 'O' and jogo[1][1] == 'O' and jogo[2][2] == 'O':
        # Esquerda para direita
        print('O jogador 2 ganhou!!!')
        exit()
    elif jogo[0][2] == 'O' and jogo[1][1] == 'O' and jogo[2][0] == 'O':
        # Direita para esquerda
        print('O jogador 2 ganhou!!!')
        exit()

print('--Jogo da Velha--')

vez = 'jogador1'
jogo = [[[]for i in range(3)] for j in range(3)]

imprimirJogo()

while True:
    aux = True
    if vez == 'jogador1':
        print('\nJogador 1 (X) escolha uma linha')

        while aux:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if jogo[linha - 1][coluna - 1] == []:
                jogo[linha - 1][coluna - 1] = 'X'
                aux = False
            else:
                print('\nEsta posição já foi escolhida.\n')
        
        imprimirJogo()
        ganhou(jogo)
        vez = 'jogador2'
    else:
        print('\nJogador 2 (O) escolha uma linha')

        while aux:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if jogo[linha - 1][coluna - 1] == []:
                jogo[linha - 1][coluna - 1] = 'O'
                aux = False
            else:
                print('\nEsta posição já foi escolhida.\n')
        
        imprimirJogo()
        ganhou(jogo)
        vez = 'jogador1'