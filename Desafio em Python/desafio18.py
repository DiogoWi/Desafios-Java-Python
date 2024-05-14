import re

print('--Validador de Email--\n')

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = input('Digite um email: ')

if(re.search(regex, email)):
    print("Email váildo.")
else:
    print("Email invalido.")