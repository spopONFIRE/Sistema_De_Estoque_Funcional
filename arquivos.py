import json
import os
from typing import List
 
from produto import Produto
 
ARQUIVO_DADOS = "dados_estoque.json"
 
 
def salvar_dados(produtos: List[Produto], caminho: str = ARQUIVO_DADOS) -> None:
    dados = [p.to_dict() for p in produtos]
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
 
 
def carregar_dados(caminho: str = ARQUIVO_DADOS) -> List[Produto]:
    if not os.path.exists(caminho):
        return []
 
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
 
    produtos = []
    for item in dados:
        try:
            produtos.append(Produto.from_dict(item))
        except (KeyError, ValueError):
            pass
 
    return produtos