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

def acao_editar() -> None:
    ui.subtitulo("Editar Produto")
    codigo = validar_codigo(ui.ler_texto("Código do produto"))
    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        ui.erro(f"Produto '{codigo}' não encontrado.")
        return
 
    ui.info(f"Produto atual: {produto}")
    ui.info("Deixe em branco para manter o valor atual.\n")
 
    try:
        nome = ui.ler_texto_opcional("Novo nome", produto.nome)
        categoria = ui.ler_texto_opcional("Nova categoria", produto.categoria)
 
        preco_str = input(f"  Novo preço [R$ {produto.preco:.2f}]: ").strip()
        preco = validar_preco(preco_str) if preco_str else produto.preco
 
        qtd_str = input(f"  Nova quantidade [{produto.quantidade}]: ").strip()
        quantidade = validar_quantidade(qtd_str) if qtd_str else produto.quantidade
 
        estoque.editar(codigo, nome=nome, preco=preco, quantidade=quantidade, categoria=categoria)
        ui.sucesso("Produto atualizado com sucesso!")
    except ValueError as e:
        ui.erro(str(e))

def acao_remover() -> None:
    ui.subtitulo("Remover Produto")
    codigo = validar_codigo(ui.ler_texto("Código do produto"))
    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        ui.erro(f"Produto '{codigo}' não encontrado.")
        return
 
    ui.info(f"Produto: {produto}")
    if ui.confirmar("Confirmar remoção?"):
        estoque.remover(codigo)
        ui.sucesso("Produto removido.")
    else:
        ui.aviso("Remoção cancelada.")

def acao_buscar_codigo() -> None:
    ui.subtitulo("Buscar por Código  [busca binária · O(log n)]")
    codigo = validar_codigo(ui.ler_texto("Código"))
    produto = estoque.buscar_por_codigo(codigo)
    if produto:
        ui.separador()
        print(ui.formatar_produto(produto))
        ui.separador()
    else:
        ui.aviso(f"Produto com código '{codigo}' não encontrado.")

def acao_buscar_nome() -> None:
    ui.subtitulo("Buscar por Nome  [busca linear · O(n)]")
    termo = ui.ler_texto("Termo de busca")
    resultados = estoque.buscar_por_nome(termo)
    if not resultados:
        ui.aviso(f"Nenhum produto encontrado com '{termo}'.")
        return
 
    ui.sucesso(f"{len(resultados)} produto(s) encontrado(s):")
    ui.separador()
    linhas = [ui.cabecalho_lista()] + [
        ui.formatar_produto(p, i + 1) for i, p in enumerate(resultados)
    ]
    ui.paginar(linhas)

def acao_registrar_venda() -> None:
    ui.subtitulo("Registrar Venda")
    codigo = validar_codigo(ui.ler_texto("Código do produto"))
    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        ui.erro(f"Produto '{codigo}' não encontrado.")
        return
 
    ui.info(f"Produto: {produto}")
    try:
        quantidade = ui.ler_inteiro("Quantidade vendida", minimo=1)
        estoque.registrar_venda(codigo, quantidade)
        total = quantidade * produto.preco
        ui.sucesso(
            f"Venda registrada! {quantidade}x '{produto.nome}' — "
            f"Total: R$ {total:.2f} | Estoque restante: {produto.quantidade}"
        )
        if produto.quantidade < LIMITE_ESTOQUE_BAIXO:
            ui.aviso(f"Atenção: estoque baixo ({produto.quantidade} unidades restantes)!")
    except ValueError as e:
        ui.erro(str(e))

def acao_listar_todos() -> None:
    ui.subtitulo("Produtos ordenados por Código")
    produtos = estoque.listar_todos()
    if not produtos:
        ui.aviso("Nenhum produto cadastrado.")
        return
 
    linhas = [ui.cabecalho_lista(), "  " + "-" * 80]
    linhas += [ui.formatar_produto(p, i + 1) for i, p in enumerate(produtos)]
    ui.paginar(linhas)
 
def acao_listar_categoria() -> None:
    ui.subtitulo("Listar por Categoria")
    cats = estoque.categorias()
    if not cats:
        ui.aviso("Nenhuma categoria cadastrada.")
        return
 
    ui.info("Categorias disponíveis: " + ", ".join(cats))
    categoria = ui.ler_texto("Categoria")
    produtos = estoque.listar_por_categoria(categoria)
    if not produtos:
        ui.aviso(f"Nenhum produto na categoria '{categoria}'.")
        return
 
    ui.sucesso(f"{len(produtos)} produto(s) em '{categoria}':")
    linhas = [ui.cabecalho_lista()] + [
        ui.formatar_produto(p, i + 1) for i, p in enumerate(produtos)
    ]
    ui.paginar(linhas)

def acao_estoque_baixo() -> None:
    ui.subtitulo(f"Estoque Baixo  (limite: {LIMITE_ESTOQUE_BAIXO} unidades)")
    produtos = estoque.estoque_baixo(LIMITE_ESTOQUE_BAIXO)
    if not produtos:
        ui.sucesso("Nenhum produto com estoque abaixo do limite.")
        return
 
    ui.aviso(f"{len(produtos)} produto(s) com estoque baixo:")
    linhas = [ui.cabecalho_lista()] + [
        ui.formatar_produto(p, i + 1) for i, p in enumerate(produtos)
    ]
    ui.paginar(linhas)

def acao_preco_minmax() -> None:
    ui.subtitulo("Relatório: Menor e Maior Preço")
    menor = estoque.menor_preco()
    maior = estoque.maior_preco()
    if menor is None:
        ui.aviso("Nenhum produto cadastrado.")
        return
 
    ui.info(f"Menor preço: {ui.formatar_produto(menor)}")
    ui.separador()
    ui.info(f"Maior preço: {ui.formatar_produto(maior)}")

def acao_salvar() -> None:
    try:
        arquivos.salvar_dados(estoque.listar_todos())
        ui.sucesso(f"Dados salvos com sucesso! ({estoque.total_produtos()} produtos)")
    except OSError as e:
        ui.erro(f"Erro ao salvar: {e}")

ACOES = {
    "1": acao_cadastrar,
    "2": acao_editar,
    "3": acao_remover,
    "4": acao_buscar_codigo,
    "5": acao_buscar_nome,
    "6": acao_registrar_venda,
    "7": acao_listar_todos,
    "8": acao_listar_categoria,
    "9": acao_estoque_baixo,
    "10": acao_preco_minmax,
}

def carregar_na_inicializacao() -> None:
    """Carrega dados do arquivo ao iniciar."""
    produtos = arquivos.carregar_dados()
    for p in produtos:
        try:
            estoque.cadastrar(p)
        except ValueError:
            pass  
    if produtos:
        ui.sucesso(f"{len(produtos)} produto(s) carregado(s) do arquivo.")

def main() -> None:
    print("\033[2J\033[H", end="") 
    carregar_na_inicializacao()
 
    while True:
        opcao = menu_principal()
        if opcao == "0":
            if ui.confirmar("Salvar antes de sair?"):
                acao_salvar()
            ui.info("Até logo!")
            sys.exit(0)
 
        acao = ACOES.get(opcao)
        if acao:
            acao()
        else:
            ui.erro("Opção inválida. Tente novamente.")
 
        input("\n  [Enter] para voltar ao menu...")
        print("\033[2J\033[H", end="") 
 
 
if __name__ == "__main__":
    main()