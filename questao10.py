'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
'''

valor = float(input("Qual o valor da prestação?: "))
taxa = float(input("Qual a taxa da prestação?: "))
tempo = float(input("Qual o tempo, em dias, da prestação?: "))

print(f'\nValor da prestação em atrasos: R${valor + (valor * (taxa / 100) * tempo)}')