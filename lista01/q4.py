from pathlib import Path

path = Path("Lista1/documentos/alunos.txt")

numero_linhas = len(path.read_text().splitlines())

print(f"o numero de linhas é {numero_linhas}")