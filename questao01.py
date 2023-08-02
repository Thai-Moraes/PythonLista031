'''
Desenvolver um programa que pergunte ao usuário o seu nome completo e seu sexo. Em seguida, o programa
deve apresentar os dados anteriormente informados.
'''

name = input("Qual o seu nome?: ")
sexo = input("Qual o seu sexo? (F/M): ")

if sexo == 'f' or sexo == 'F':
    sexo = sexo + ' (♀)'
else:
    sexo = sexo + ' (♂)'

print(f'\nO seu nome é {name}\nO seu sexo é {sexo}')

