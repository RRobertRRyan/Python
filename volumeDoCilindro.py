import math

raio = int(input("Qual o raio da base: "))
altura = int(input("Qual a altura do cilindro: "))

base = math.pi * raio ** 2
resultado = base * altura

print(f"O volume do cilindro é: {resultado:.2f}")