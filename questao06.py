'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
temperatura convertida em graus Celsius. A fórmula da conversão é c	=	(f	–	32)	x	5	:	9	, onde c	 é a temperatura
em graus Celsius e f		em Fahrenheit
'''

fahrenheit = float(input("Informe temperatura em graus Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f'{fahrenheit}°F convertido para Celsius é igual a {celsius}°C')