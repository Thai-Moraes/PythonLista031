'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro
'''

dist = float(input("Distância a percorrer na viagem (km): "))
consumo = float(input("Consumo médio do automóvel (km por l): "))

print(f"Litros que o automóvel gastará: {consumo * dist}l")