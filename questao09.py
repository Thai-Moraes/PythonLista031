import math

'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''

num = float(input("Informe um número: "))

print(f'\nO próprio número: {num}\nO quadrado deste número: {math.pow(num, 2)}\nA raiz quadrada deste número: {math.sqrt(num)}')