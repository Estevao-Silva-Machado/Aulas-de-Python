n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print(f'O primeiro valor que você digitou é maio, pois {n1:.1f} é maior do que {n2:.1f}.')

elif n2 > n1:
    print(f'O segundo valor que você digitou é maior, pois {n2:.1f} é maior do que {n1:.1f}.')

else:
    print(f'Os valores {n1:.1f} e {n2:.1f} são exatamente iguais!')