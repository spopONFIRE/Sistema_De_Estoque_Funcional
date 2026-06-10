from produto import Produto
from typing import List, Optional
import bisect

class Estoque:
    def __init__(self):
        self._produtos_ord: List[Produto] = [] 
        self._codigos_ord: List[str] = []      

    def cadastrar(self, produto: Produto) -> None:
        idx = bisect.bisect_left(self._codigos_ord, produto.codigo)
        if idx < len(self._codigos_ord) and self._codigos_ord[idx] == produto.codigo:
            raise ValueError(f"Código '{produto.codigo}' já cadastrado.")
        self._codigos_ord.insert(idx, produto.codigo)
        self._produtos_ord.insert(idx, produto)   