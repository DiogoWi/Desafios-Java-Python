def celsiusFahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit, '°F.')

def fahrenheitCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(celsius, '°C.')

def quilometrosMilhas(quilometros):
    milhas = quilometros / 1.609
    print(milhas, 'mi.')

def milhasQuilometros(milhas):
    quilometros = milhas * 1.609
    print(quilometros, 'km.')

def kmHoraMSegundo(kmH):
    mS = kmH / 3.6
    print(mS, 'm/s.')

def mSegundoKmHora(mS):
    kmH = mS * 3.6
    print(kmH, 'km/h.')

print("""--Conversor de Unidades--
\nAlternativas:
1 - Celsius para Fahrenheit.
2 - Fahrenheit para Celsius.
3 - quilômetros para milhas.
4 - milhas para quilômetros.
5 - km/h para m/s.
6 - m/s para km/h.""")

aux = True

while aux:
    opcao = int(input('\nEscolha uma alternativa: '))

    if opcao <= 0 or opcao >= 7:
        print('Esta alternativa não existe.')
    else:
        aux = False

if opcao == 1:
    celsius = float(input('Digite os graus Celsius: '))
    celsiusFahrenheit(celsius)
elif opcao == 2:
    fahrenheit = float(input('Digite os graus Fahrenheit: '))
    fahrenheitCelsius(fahrenheit)
elif opcao == 3:
    quilometros = float(input('Digite os quilômetros: '))
    quilometrosMilhas(quilometros)
elif opcao == 4:
    milhas = float(input('Digite as milhas: '))
    milhasQuilometros(milhas)
elif opcao == 5:
    kmH = float(input('Digite os km/h: '))
    kmHoraMSegundo(kmH)
elif opcao == 6:
    mS = float(input('Digite os m/s: '))
    mSegundoKmHora(mS)