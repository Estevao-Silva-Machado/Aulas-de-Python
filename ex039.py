from datetime import date
atual = date.today().year
nascimento = int(input('Que ano você nasceu? '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {atual}.')

if idade == 18:
    print('Já está na hora de você fazer seu alistamento')

elif idade < 18:
    tempo = 18 - idade
    listamento = atual + tempo
    print(f'Ainda faltam {tempo} para seu alistamento')
    print(f'Seu alistamento será em {listamento}.')

elif idade > 18:
    tempo = idade - 18
    listamento = atual - tempo
    print(f'Você deveria ter se alistado há {tempo} anos.')
    print(f'Seu alistasmento foi em {listamento}.')

else:
    print('Algo deu Errado!')
