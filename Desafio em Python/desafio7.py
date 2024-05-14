def contarPalavra(texto):
    palavras = 0

    for i in texto:
        palavras += 1

    print('O seu texto tem', palavras, 'palavras.')

print('--Contador de Palavras--\n')

texto = input('Digite o texto: ')
contarPalavra(texto.split())