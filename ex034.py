salario = float(input('Qual é seu salário? R$'))

''' Para salarios acima de 1.250,00 o aumento será de 10%
    Para inferiores a 1.250,00 o aumento será de 15%      '''

if salario <= 1250.00:
    aumento = (salario * 15 / 100) + salario
else:
    aumento = (salario * 10 / 100) + salario

print('O seu salário de R${:.2f}, passará a ser R${:.2f}'.format(salario, aumento))
