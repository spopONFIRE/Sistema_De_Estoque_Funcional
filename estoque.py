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

    def buscar_por_codigo(self, codigo: str) -> Optional[Produto]:
        codigo = codigo.strip().upper()
        idx = bisect.bisect_left(self._codigos_ord, codigo)
        if idx < len(self._codigos_ord) and self._codigos_ord[idx] == codigo:
            return self._produtos_ord[idx]
        return None
    
    def _indice_por_codigo(self, codigo: str) -> int:
        idx = bisect.bisect_left(self._codigos_ord, codigo)
        if idx < len(self._codigos_ord) and self._codigos_ord[idx] == codigo:
            return idx
        return -1
    def buscar_por_nome(self, termo: str) -> List[Produto]:
        termo = termo.strip().lower()
        return [p for p in self._produtos_ord if termo in p.nome.lower()]

def editar(
        self,
        codigo: str,
        nome: Optional[str] = None,
        preco: Optional[float] = None,
        quantidade: Optional[int] = None,
        categoria: Optional[str] = None,
    ) -> Produto:
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise ValueError(f"Produto com código '{codigo}' não encontrado.")
        if nome is not None:
            produto.nome = nome.strip()
        if preco is not None:
            if preco <= 0:
                raise ValueError("Preço deve ser positivo.")
            produto.preco = preco
        if quantidade is not None:
            if quantidade < 0:
                raise ValueError("Quantidade não pode ser negativa.")
            produto.quantidade = quantidade
        if categoria is not None:
            produto.categoria = categoria.strip()
        return produto
 
    def remover(self, codigo: str) -> Produto:
        """
        Remove produto pelo código.
        Complexidade: O(log n) busca + O(n) deslocamento = O(n).
        """
        idx = self._indice_por_codigo(codigo.strip().upper())
        if idx == -1:
            raise ValueError(f"Produto com código '{codigo}' não encontrado.")
        produto = self._produtos_ord.pop(idx)
        self._codigos_ord.pop(idx)
        return produto
  
    def registrar_venda(self, codigo: str, quantidade: int) -> Produto:
        if quantidade <= 0:
            raise ValueError("Quantidade da venda deve ser maior que zero.")
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise ValueError(f"Produto com código '{codigo}' não encontrado.")
        if produto.quantidade < quantidade:
            raise ValueError(
                f"Estoque insuficiente. Disponível: {produto.quantidade}, "
                f"solicitado: {quantidade}."
            )
        produto.quantidade -= quantidade
        return produto
 
    def listar_todos(self) -> List[Produto]:
        return list(self._produtos_ord)
 
    def listar_por_categoria(self, categoria: str) -> List[Produto]:
        cat = categoria.strip().lower()
        return [p for p in self._produtos_ord if p.categoria.lower() == cat]
 
    def estoque_baixo(self, limite: int = 5) -> List[Produto]:
        return [p for p in self._produtos_ord if p.quantidade < limite]
 
    def menor_preco(self) -> Optional[Produto]:
        if not self._produtos_ord:
            return None
        return min(self._produtos_ord, key=lambda p: p.preco)
 
    def maior_preco(self) -> Optional[Produto]:
        if not self._produtos_ord:
            return None
        return max(self._produtos_ord, key=lambda p: p.preco)
 
    def categorias(self) -> List[str]:
        return sorted({p.categoria for p in self._produtos_ord})
 
    def total_produtos(self) -> int:
        return len(self._produtos_ord)