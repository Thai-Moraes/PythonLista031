'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
'''

valor = float(input("Qual o valor original?: "))
taxa = float(input("Qual é a taxa?: "))
tempo = float(input("Qual o tempo em dias?: "))

print(f'\nValor da prestação em atraso: R${valor + (valor * (taxa / 100) * tempo)}')