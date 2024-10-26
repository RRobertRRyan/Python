
from pathlib import Path

# Define o caminho do arquivo
caminho_do_arquivo = Path("meus_dados.txt")

# Dados para salvar no arquivo
dados_para_salvar = ["Marília", "Dani", "Ryan"]

# Abre o arquivo no modo 'w' (escrita) e salva os dados
with caminho_do_arquivo.open(mode='w') as arquivo:
    for item in dados_para_salvar:
        arquivo.write(f"{item}\n")

# Formata os dados para imprimir na tela
nomes_formatados = ", ".join(dados_para_salvar)
print(f"Os nomes são: {nomes_formatados}")

print("Dados salvos com sucesso!")

# Abre o arquivo no modo 'r' (leitura) e lê os dados
with caminho_do_arquivo.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()

# Remove os caracteres de nova linha
dados_lidos = [linha.strip() for linha in dados_lidos]

print("Dados lidos do arquivo:", dados_lidos)