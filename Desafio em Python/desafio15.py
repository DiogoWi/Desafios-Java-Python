import time
import os

print('--Cronômetro--\n')

hora = int(input('Digite a quantidade de horas: '))
minuto = int(input('Digite a quantidade de minutos: '))
segundo = int(input('Digite a quantidade de segundos: '))

if segundo > 59:
    minuto += int(segundo / 60)
    segundo -= int(segundo / 60) * 60

if minuto > 59:
    hora += int(minuto / 60)
    minuto -= int(minuto / 60) * 60

for i in range(hora + 1):
    for j in range(minuto + 1):
        for k in range(segundo + 1):
            os.system('cls')
            print('{:02}:'.format(hora), '{:02}:'.format(minuto), '{:02}'.format(segundo), sep='')
            segundo -= 1
            time.sleep(1)

        minuto -= 1
        segundo = 59
    
    hora -= 1
    minuto = 59

print('Tempo acabou.')