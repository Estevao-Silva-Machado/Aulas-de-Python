import datetime
year = datetime.datetime.today().year
day = datetime.datetime.today().day
month = datetime.datetime.today().month
print(f'Data: {day}/{month}/{year}.')
ano = int(input('Ano de Nascimento: '))
idade = year - ano
print(f'O atleta tem {idade} anos!')

if idade <= 9:
    c = 'MIRIM'
elif idade <= 14:
    c = 'INFANTIL'
elif idade <= 19:
    c = 'JUNIOR'
elif idade <= 25:
    c = 'SÊNIOR'
elif idade > 25:
    c = 'MASTER'

print(f'Classificação: {c}')