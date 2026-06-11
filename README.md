# Sistema de Estoque e Vendas

Sistema de controle de produtos, vendas e relatórios via terminal, desenvolvido em Python.

---

# Objetivo
Construir um sistema de linha de comando para controlar produtos, vendas e relatorios. O projeto deve aplicar conteudos das secoes 2 a 5 (Python basico, Big-O, vetores nao ordenados e vetores ordenados).

---

## Requisitos

- Interface por terminal com menu claro.
- Dados persistidos em arquivo.
- Codigo organizado em modulos e funcoes.
- Tratamento de erros de entrada (numero, texto, vazio).
- Complexidade explicada: justificar uso de busca linear e binaria.

---

## Como executar

```bash
git clone https://github.com/spopONFIRE/Sistema_De_Estoque_Funcional.git
cd Sistema_De_Estoque_Funcional

python main.py
```

O arquivo `dados_estoque.json` de exemplo já inclui 10 produtos para teste.
Na primeira execução, os dados são carregados automaticamente.

---

## Estrutura do projeto

```
├── main.py        # Menu principal e fluxo da aplicação
├── produto.py     # Classe Produto e validações
├── estoque.py     # Operações de cadastro, busca e gestão
├── arquivos.py    # Persistência de dados em JSON
├── ui.py          # Utilitários de interface 
└── dados_estoque.json  # Arquivo de dados 
```

---

## Funcionalidades

| Opção | Funcionalidade |
|-------|----------------|
| 1 | Cadastrar produto (código único) |
| 2 | Editar produto (nome, preço, quantidade, categoria) |
| 3 | Remover produto |
| 4 | Buscar por código — **busca binária O(log n)** |
| 5 | Buscar por nome — **busca linear O(n)** |
| 6 | Registrar venda (valida estoque) |
| 7 | Listar todos ordenados por código |
| 8 | Listar por categoria |
| 9 | Relatório de estoque baixo (limite configurável) |
| 10 | Relatório menor/maior preço |
| 01 | Sair

---

## Exemplos de uso

### Cadastrar produto
```
Opção: 1
  Código: PROD999
  Nome: Mochila Impermeável 30L
  Categoria: Acessórios
  Preço (R$): 189,90
  Quantidade: 25
  ✔ Produto 'Mochila Impermeável 30L' cadastrado com sucesso!
```

### Buscar por código
```
Opção: 4
  Código: ELET002
  ── Busca binária · O(log n) ──
      ELET002        Carregador USB-C 65W         Eletrônicos       R$    149.90  Qtd: 3
```

### Registrar venda
```
Opção: 6
  Código: LIVR006
  Produto: [LIVR006] Python Fluente - 2ª Ed. | R$ 119.90 | Qtd: 8
  Quantidade vendida: 3
  ✔ Venda registrada! 3x 'Python Fluente' — Total: R$ 359.70 | Estoque restante: 5
```

---

## Relatório de escolhas técnicas

### Busca e ordenação

**Vetor ordenado por código** — os produtos são mantidos em ordem alfabética pelo código usando bisect, permitindo busca binária com complexidade O(log n).

**Busca por nome** — percorre todos os produtos em O(n), pois não há como aproveitar ordenação para buscas por substring.

**Inserção e remoção** — O(n) devido ao deslocamento de elementos no vetor após a posição de inserção/remoção.

### Regras de negócio

- Código de produto deve ser único
- Não é permitido registrar venda com estoque insuficiente
- Preço deve ser positivo
- Quantidade não pode ser negativa

### Big-O resumido

| Operação | Complexidade | Justificativa |
|---|---|---|
| Buscar por código | O(log n) | Busca binária em vetor ordenado |
| Buscar por nome | O(n) | Varredura linear por substring |
| Cadastrar | O(n) | Inserção ordenada com deslocamento |
| Remover | O(n) | Busca O(log n) + deslocamento O(n) |
| Editar | O(log n) | Busca binária + atualização in-place |
| Listar todos | O(1) | Vetor já ordenado, retorno direto |
| Filtrar por categoria | O(n) | Varredura completa necessária |
| Menor/maior preço | O(n) | Comparação de todos os preços |

---

## Persistência

Os dados são salvos automaticamente em `dados_estoque.json` ao sair do sistema. Ao iniciar, o arquivo é carregado automaticamente se existir.

---

