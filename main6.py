#while

senha_correta = 'python12'
tentativa = ''

print("bem vindo! por favor, digite a sua senha.")

while tentativa != senha_correta:
    tentativa = input('digite a senha:')
    if tentativa != senha_correta:
        print('senha incorreta. tenta novamente.')

print('senha correta! acesso permitido.')