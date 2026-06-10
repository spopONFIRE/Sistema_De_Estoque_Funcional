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

def ler_texto(prompt: str, obrigatorio: bool = True) -> str:
    while True:
        valor = input(f"  {prompt}: ").strip()
        if valor:
            return valor
        if not obrigatorio:
            return ""
        erro("Campo obrigatório. Tente novamente.")
 
def ler_texto_opcional(prompt: str, atual: str = "") -> str:
    dica = f" [{atual}]" if atual else ""
    valor = input(f"  {prompt}{dica}: ").strip()
    return valor if valor else atual
 
def ler_inteiro(prompt: str, minimo: int = 0, maximo: Optional[int] = None) -> int:
    while True:
        try:
            valor = int(input(f"  {prompt}: ").strip())
            if valor < minimo:
                erro(f"Valor mínimo: {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                erro(f"Valor máximo: {maximo}.")
                continue
            return valor
        except ValueError:
            erro("Informe um número inteiro válido.")
 
def ler_float(prompt: str, minimo: float = 0.01) -> float:
    while True:
        try:
            valor = float(input(f"  {prompt}: ").replace(",", ".").strip())
            if valor < minimo:
                erro(f"Valor mínimo: {minimo:.2f}.")
                continue
            return valor
        except ValueError:
            erro("Informe um número válido (ex: 9.99 ou 9,99).")
 
def confirmar(prompt: str) -> bool:
    resp = input(f"  {prompt} (S/N): ").strip().upper()
    return resp == "S"

TAMANHO_PAGINA = 10
 
 
def paginar(linhas: List[str], tamanho: int = TAMANHO_PAGINA) -> None:
    total = len(linhas)
    if total == 0:
        aviso("Nenhum item para exibir.")
        return
 
    inicio = 0
    pagina = 1
    total_paginas = (total + tamanho - 1) // tamanho
 
    while inicio < total:
        fim = min(inicio + tamanho, total)
        for linha in linhas[inicio:fim]:
            print(linha)
        print(f"\n  Página {pagina}/{total_paginas} | {total} item(s) no total")
 
        if fim >= total:
            break
        resp = input("  [Enter] próxima página | [Q] sair: ").strip().upper()
        if resp == "Q":
            break
        inicio = fim
        pagina += 1
 
def formatar_produto(p, numero: Optional[int] = None) -> str:
    prefixo = f"{numero:>3}. " if numero is not None else "    "
    return (
        f"{prefixo}"
        f"{p.codigo:<12} "
        f"{p.nome:<28} "
        f"{p.categoria:<16} "
        f"R$ {p.preco:>8.2f}  "
        f"Qtd: {p.quantidade}"
    )
 
 
def cabecalho_lista() -> str:
    return f"    {'CÓDIGO':<12} {'NOME':<28} {'CATEGORIA':<16} {'PREÇO':>11}  ESTOQUE"