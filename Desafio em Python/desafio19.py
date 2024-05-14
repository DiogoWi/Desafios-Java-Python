print("""--Conversor de Moeda--

Opçõens:
1 - Iene
2 - Dólar
3 - Euro\n""")

dinheiro = float(input('Quanto dinheiro você tem: '))
aux = True

while aux:
    conversao = int(input('Escolha para qual moeda você quer converter com o número da opção: '))

    if conversao >= 1 and conversao <= 3:
        aux = False

if conversao == 1:
    conversao_iene = dinheiro / 0.033 #convertendo para iene

    print(f'Com {dinheiro:.2f} reais você pode comprar {conversao_iene:.2f} ienes.')
elif conversao == 2:
    conversao_dolar = dinheiro * 5.00 #convertendo para dolar

    print(f'Com {dinheiro:.2f} reais você pode comprar {conversao_dolar:.2f} dólar.')
elif conversao == 3:
    conversao_euro = dinheiro * 5.43 #convetrendo para euro

    print(f'Com {dinheiro:.2f} reais você pode comprar {conversao_euro:.2f} euro.')