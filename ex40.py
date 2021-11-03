nota01 = float(input('Qual foi sua Primeira nota? '))
nota02 = float(input('Qual foi sua Segunda nota? '))
media = (nota01 + nota02) / 2
print(f'Tirando {nota01} e {nota02}, a média do aluno é {media:.1f}.')

if media >= 7.0:
    r = 'APROVADO'
    print(f'O aluno está {r}!')
elif media < 5.0:
    r = 'REPROVADO'
    print(f'O aluno está {r}!')
elif 7 > media >= 5:#Se a média for entre 5 e 7 oaluno estará em recuperação (é um pouco complicado, mas nada que eu não possa fazer.)
    print('O aluno está em RECUPERAÇÃO')
#elif media >= 5 and media < 7: #Se a média for entre 5 e 7 oaluno estará em recuperação
#    print(f'O aluno está em RECUPERAÇÃO!')


