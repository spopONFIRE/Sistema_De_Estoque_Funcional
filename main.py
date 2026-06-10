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
    print("[11] Salvar dados:")
    print("[12] onfigurar limitjine de estoque baixo:")
    print("---------------------------------------")
    print("[0] Sair")
    print("---------------------------------------")
    return input("Digite sua opção:")