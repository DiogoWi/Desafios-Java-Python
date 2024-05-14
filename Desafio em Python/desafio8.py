import re

print('--Validador de Senha Forte--\n')

senha = input('Digite uma senha: ')

# Verificação números de caracteres
if len(senha) < 8:
    print('\n\033[31mDeve conter no mínimo 8 caracteres.\033[m')
else:
    print('\n\033[32mContem o mínimo de caracteres.\033[m')

# Verificação de maiúsculos
if any(i.isupper() for i in senha):
    print('\033[32mMínimo de caracteres maiúsculos atingido.\033[m')
else:
    print('\033[31mDeve conter no mínimo 1 caracter maiúsculo.\033[m')

# Verificação de minúsculos
if re.search('[a-z]', senha):
    print('\033[32mMínimo de caracteres minúsculos atingido.\033[m')
else:
    print('\033[31mDeve conter no mínimo 1 caracter minúsculo.\033[m')

# Verificação de números
if re.search('[0-9]', senha):
    print('\033[32mMínimo de números atingido.\033[m')
else:
    print('\033[31mDeve conter no mínimo 1 número.\033[m')

# Verificação de caracteres especiais
if re.search('[!-/:-@[-`]', senha):
    print('\033[32mMínimo de caracter especial atingido.\033[m')
else:
    print('\033[31mDeve conter no mínimo 1 caracter especial.\033[m')