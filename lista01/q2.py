from pathlib import Path

arquivo = input("Digite o nome do arquivo: ")

path = Path(arquivo)

if path.is_file(): #cria objeto pathlib
    print(f"o arquivo {arquivo} exite")
else:
    print(f"o arquivo {arquivo} não existe")
