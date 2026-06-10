import sys

import arquivos
import ui
from estoque import Estoque
from produto import Produto, validar_codigo, validar_preco, validar_quantidade

estoque = Estoque()
LIMITE_ESTOQUE_BAIXO = 5

def menu_principal() -> str:    
    print("[1] Cadastrar produto:")
    print("[2] Editar produto:")
    print("[3] Remover produto:")
    print("[4] Buscar produto por código:")
    print("[5] Buscar produtos por nome:")
    print("[6] Registrar venda:")
    print("---------------------------------------")
    print("[7] Listar produtos:")
    print("[8] Listar por categoria:")
    print("[9] Relatório de estoque baixo:")
    print("[10] Relatório: menor e maior preço:")
    print("---------------------------------------")
    print("[0] Sair")
    print("---------------------------------------")
    return input("Digite sua opção:")

def acao_cadastrar() -> None:
    ui.subtitulo("Cadastrar Produto")
    try:
        codigo = validar_codigo(ui.ler_texto("Código"))
        nome = ui.ler_texto("Nome")
        categoria = ui.ler_texto("Categoria")
        preco = ui.ler_float("Preço (R$)", minimo=0.01)
        quantidade = ui.ler_inteiro("Quantidade", minimo=0)
 
        produto = Produto(codigo, nome, categoria, preco, quantidade)
        estoque.cadastrar(produto)
        ui.sucesso(f"Produto '{nome}' cadastrado com sucesso!")
    except ValueError as e:
        ui.erro(str(e))

# def acao_editar() -> None: # 

# def acao_remover() -> None: # 

# def acao_buscar_codigo() -> None: # 

# def acao_buscar_nome() -> None: # 

# def acao_registrar_venda() -> None: # 

# def acao_listar_todos() -> None: # 

# def acao_listar_categoria() -> None: # 

# def acao_estoque_baixo() -> None: # 

# def acao_preco_minmax() -> None: # 