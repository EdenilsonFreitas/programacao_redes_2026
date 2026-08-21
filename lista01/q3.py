
from pathlib import Path

path = Path(__file__).parent / "documentos" / "nomes.txt"

conteudo = path.read_text()

print(conteudo)
