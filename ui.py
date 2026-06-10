from typing import List, Optional

def titulo(texto: str) -> None:
    largura  = 45
    print()
    print("=" * largura)
    print(f"  {texto}")
    print("=" * largura)

def subtitulo(texto: str) -> None:
    print(f"\n-- {texto} --")
 
def sucesso(texto: str) -> None:
    print(f"  [OK] {texto}")
 
def erro(texto: str) -> None:
    print(f"  [ERRO] {texto}")
 
def aviso(texto: str) -> None:
    print(f"  [AVISO] {texto}")
 
def info(texto: str) -> None:
    print(f"  {texto}")
 
def separador() -> None:
    print("  " + "-" * 40)