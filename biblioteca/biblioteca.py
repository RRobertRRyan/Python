# Uma biblioteca para armazenar dados

from pathlib import Path 

caminho_do_arquivo = Path("cliente.biblioteca.txt")

nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
numero_do_cartao = input("Digite o numero do seu cartão: ")

with caminho_do_arquivo.open(mode='a') as arquivo:
    arquivo.write(f"{nome}, {telefone}, {numero_do_cartao}\n")

    print("cliente cadastrado com sucesso!")
