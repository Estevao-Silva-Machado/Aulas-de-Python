#Exercicío 36 do mundo 02 de Python do Canal do Curs em Video
#O programa terá que fazer a verificação, se o cliente do banco está apto a fazer um emprestimo
#Seguindo os seguintes critérios:
#O valor das parcelas não poderá exeder de 30% do salário mensal do cliente
#Para isso precisaremos que o usuario informe salário do cliente em quantos ano o ciente terá que ficar pagando
#o emprestime e o valor do emprestimo
# O programa se resposabilizara em: Informar se o cliente poderá fazer o emprestimo e qual será o valor das parcelas a
#ser pagas todos os meses.
casa = int(input('Qual é o valor da casa? R$'))
salario = int(input('Qual é o salário do cliente? R$'))
tempo = int(input('Em quantos anos será pago esse imóvel? '))
parcelas = casa / (tempo * 12)
porcentagem = 30/100 * salario
print('Eu sou', end='') #Função end servirá para colocar na mesma linha os dois print
print(' lindo')

if parcelas > porcentagem:
    print('Seu emprestimeo foi {}negado{}'.format('\033[4;31m', '\033[m'))
    print('Pois o valor das parcelas é: {:.2f}, onde exede de 30% que é de {:.2f}!'.format(parcelas, porcentagem))
    print('Infelismente o valor das parcelar não irá caber no seu bolso!')
    print('Tente fazer novamente o teste, aumentando os anos!')
elif parcelas <= porcentagem:
    print('Seu pedido de emrestimo foi {}aprovado{}'.format('\033[4;32m', '\033[m'))
    print('O valor das parcelas mensais será de: R${:.2f}'.format(parcelas))
else:
    print('Ops! Algo deu errado, favor tente novamente')


