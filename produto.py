from typing import Optional
from dataclasses import dataclass

@dataclass
class Produto:
    codigo: str
    nome: str
    categoria: str
    preco: float
    quantidade: int

    def __post_init__(self):
        self.validar()

    def validar(self) -> None:
        if not self.codigo or not self.codigo.strip():
            raise ValueError("Código não pode ser vazio.")
        if not self.nome or not self.nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        if not self.categoria or not self.categoria.strip():
            raise ValueError("Categoria não pode ser vazia.")
        if self.preco <= 0:
            raise ValueError("Preço deve ser positivo.")
        if self.quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        
    def to_dict(self) -> dict:
        return{
            "codigo": self.codigo, "nome": self.nome, "categoria": self.categoria,
            "preco": self.preco, "quantidade": self.quantidade,
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Produto":
        return Produto(
            codigo=data["codigo"],
            nome=data["nome"],
            categoria=data["categoria"],
            preco=float(data["preco"]),
            quantidade=int(data["quantidade"]),
        )

    def __str__(self) -> str:
        return (
            f"[{self.codigo}] {self.nome} | "
            f"Categoria: {self.categoria} | "
            f"Preço: R$ {self.preco:.2f} | "
            f"Qtd: {self.quantidade}"
        )
    
def validar_codigo(codigo: str) -> str:
    codigo = codigo.strip().upper()
    if not codigo:
        raise ValueError("Código não pode ser vazio.")
    return codigo

def validar_preco(valor: str) -> float:
    try:
        preco = float(valor.replace(",", "."))
    except (ValueError, AttributeError):
        raise ValueError("Preço inválido. Use um número positivo.")
    if preco <= 0:
        raise ValueError("Preço deve ser positivo.")
    return preco

def validar_quantidade(valor: str) -> int:
    try:
        qtd = int(valor)
    except (ValueError, AttributeError):
        raise ValueError("Quantidade inválida. Use um número inteiro.")
    if qtd < 0:
        raise ValueError("Quantidade não pode ser negativa.")
    return qtd
