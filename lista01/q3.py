
from pathlib import Path

path = Path("Lista1/documentos/nomes.txt")

conteudo = path.read_text()

print(conteudo)
