#GAMER: JO KEN PO!!! (Pedra Papel Tesoura)
from random import randint
from time import sleep
escolha = ['Nada', 'Pedra', 'Papel', 'Tesoura']
c = randint(1, 3) #O computador está escolhendo o que irá ussar (Pedra Papel Tesoura)
print('''
Suas Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
u = int(input('Qual é sua jogada? '))

if u <= 3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=' * 15)
    print(f'O COMPUTADOR escolheu {escolha[c]}')
    print(f'O JOGADOR escolheu {escolha[u]}')
    print('-=' * 15)

    motivo = [
        'Pedra QUEDRA a Tesoura!',
        'Papel COBRE a Pedra!',
        'Tesoura CORTA Papel'
    ]

    if c == u:
        print('EMPATE')

    elif c == 1:#computador escolheu Pedra
        if u == 2: #Usuário escolheu Papel
            print(motivo[1])
            print('O JOGADOR VENCEU!')

        elif u == 3:#Usuário escolheu Tesoura
            print(motivo[0])
            print('O JOGADOR PERDEU!')

        else:
            print('JOGADA INVÁLIDA')

    elif c == 2:  # computador escolheu Papel
        if u == 1:  # Usuário escolheu Pedra
            print(motivo[1])
            print('O JOGADOR PERDEU!')

        elif u == 3:  # Usuário escolheu Tesoura
            print(motivo[2])
            print('O JOGADOR VENCEU!')

        else:
            print('JOGADA INVÁLIDA')

    elif c == 3:  # computador escolheu Tesoura
        if u == 1:  # Usuário escolheu Pedra
            print(motivo[0])
            print('O JOGADOR VENCEU!')

        elif u == 2:  # Usuário escolheu Papel
            print(motivo[2])
            print('O JOGADOR PERDEU!')

        else:
            print('JOGADA INVÁLIDA')

else:
    print('''
    ALGO DEU ERRADO!!!
    TENTE NOVAMENTE.
    ''')
