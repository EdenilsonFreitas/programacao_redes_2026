
"""
 o Operador / permite concatenar paths. Isso ajuda a definir caminhos para explorar pastas e arquivos.
 IMPORTANTE >> Ele tem esse uso apenas quando utilizado junto a pathlib.
"""
from pathlib import Path
arquivo = Path('.')  / "lista1" / "documentos" / "relatorio.txt"
print(arquivo)
print(arquivo.is_file())# informa se é um arquivo
print(arquivo.exists()) # informa se é um path valido (arquivos ou dir)
print(arquivo.is_dir()) # informa se é um diretorio

