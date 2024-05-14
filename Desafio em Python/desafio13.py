print('--Calculadora de Juros Compostos--\n')

# Formula:
# M = C(1 + i)^n
# M = Montante
# C = Capital Aplicado
# i = Taxa de juros composto
# n = Tempo de aplicação
# J = juros composto: M - C

capital = float(input('Capital inicial: '))
# mensal = float(input('Capital mensal: '))
taxa = float('%.2f' % (float(input('Taxa de juros anual: ')) / 100))
tempo = float(input('Período em anos: '))

montante = capital * (1 + taxa) ** tempo

print('\nValor total final: R$%.2f' % montante)
print('Valor total investido: R$%.2f' % capital)
print('Total em juros: R$%.2f' % (montante - capital))