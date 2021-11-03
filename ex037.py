#Escreva um programa que leia um número inteiro e peça para o usuário escolher qual sera a base de conversão
p = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para para BINÁRIO
[ 2 ] Converter para para OCTAL
[ 3 ] Converter para para HEXADECIMAL''')
opcao = int(input('sua opção: '))
m = 1

if opcao == 1:
    print(f'{p} convertido para BINÁRIO é igual à {bin(p) [2:]}')

elif opcao == 2:
    print(f'{p} convertido para OCTAL é igual à {oct(p) [2:]}')

elif opcao == 3:
    print(f'{p} convertido para HEXADECIMAL é igual à {hex(p) [2:]}')

else:
    print('Ops! Algo deu errado, favor tente novamente')
