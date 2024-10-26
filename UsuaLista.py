# Listas

frutas = []

while True :
    fruta = input("digite o nome de uma fruta ou sair: ")
    if fruta.lower() == 'sair' :
        break

    frutas.append(fruta)

print("Lista de frutas :")
for fruta in frutas:
    print(fruta)
