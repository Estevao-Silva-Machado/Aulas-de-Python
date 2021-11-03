print("Exercicío nº 0031")
distancia = float(input('Qual é a distancia de sua viagem?'))
print('Você está preste a começar uma viajem de {}Km'.format(distancia))

'''
if distancia <= 200:
    preço = distancia * 0.50

else:
    preço = distancia * 0.45
'''
#ou
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da sua passagem será de R${:.2f} reais!'.format(preço))
