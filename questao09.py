import math

'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''

num = float(input("Informe um número: "))

print(f'\nO próprio número é: {num}\nO quadrado deste número é: {math.pow(num, 2)}\nA raiz quadrada deste número é: {math.sqrt(num)}')