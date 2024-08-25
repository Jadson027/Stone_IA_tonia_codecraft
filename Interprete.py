import pandas as pd
import os
from glob import glob

# Função para analisar o comando do usuário e extrair palavras-chave
def interpretar_comando(comando):
    palavras_chave = {
        "tipo_transacao": None,
        "mes": None,
        "categoria": None,
        "descricao": None,
        "metodo_pagamento": None,
        "detalhamento": None,
        "cancelar": False
    }

    comando = comando.lower()

    # Variáveis para tipo de transação
    transacao_recebimento = [
        "recebimento", "recebimentos", "entradas", "ganhos", "recebi", 
        "receber", "faturamento", "faturei", "créditos", "creditos", 
        "depósitos", "deposito", "entrar dinheiro", "receita", 
        "receitas", "entrada de caixa", "dinheiro recebido", "vendas", 
        "faturamento bruto", "faturamento total", "renda", "rendimentos"
    ]
    
    transacao_pagamento = [
        "pagamento", "pagamentos", "saídas", "saída", "gastos", 
        "paguei", "pagar", "compras", "comprei", "debitos", 
        "débitos", "insumos", "compra", "comprando", "despesas", 
        "despesa", "contas pagas", "contas a pagar", "desembolso", 
        "dinheiro gasto", "saiu do caixa", "despesas operacionais", 
        "despesas fixas", "despesas variáveis", "custos", 
        "custos fixos", "custos variáveis", "pagamento de fornecedores",
        "compra de equipamentos", "equipamentos", "pagamento de impostos", 
        "imposto", "impostos", "compra de insumos", "luz", "venda", "vendas"
    ]
    
    transacao_completo = [
        "total", "geral", "completo", "tudo", "toda", 
        "consolidado", "consolidei", "balanço", "balanco", 
        "resumo", "resumo geral", "totalizador", "fechamento", 
        "fechamento mensal", "fechar mês", "resultado completo", 
        "resultado geral", "predial", "reparos", "produtos"
    ]

    # Variáveis para cancelar
    cancelar_opcoes = [
        "cancelar", "menu", "menu principal", "não quero", 
        "não é isso", "nao quero", "nao é isso", "abortar", 
        "sair", "desistir", "parar", "interromper", "voltar", 
        "resetar", "reiniciar", "desfazer", "cancela isso"
    ]

    # Verificar se o usuário deseja cancelar
    if any(palavra in comando for palavra in cancelar_opcoes):
        palavras_chave["cancelar"] = True
        return palavras_chave

    # Identificar tipo de transação
    if any(palavra in comando for palavra in transacao_recebimento):
        palavras_chave["tipo_transacao"] = "recebimento"
    elif any(palavra in comando for palavra in transacao_pagamento):
        palavras_chave["tipo_transacao"] = "pagamento"
    elif any(palavra in comando for palavra in transacao_completo):
        palavras_chave["tipo_transacao"] = "completo"

    # Variáveis para mês
    meses = {
        "janeiro": "2025-01", "fevereiro": "2025-02", "março": "2025-03", 
        "abril": "2025-04", "maio": "2025-05", "junho": "2025-06", 
        "julho": "2025-07", "agosto": "2025-08", "setembro": "2025-09", 
        "outubro": "2025-10", "novembro": "2025-11", "dezembro": "2025-12",
        "primeiro mês": "2025-01", "segundo mês": "2025-02", "terceiro mês": "2025-03",
        "quarto mês": "2025-04", "quinto mês": "2025-05", "sexto mês": "2025-06",
        "sétimo mês": "2025-07", "oitavo mês": "2025-08", "nono mês": "2025-09",
        "décimo mês": "2025-10", "undécimo mês": "2025-11", "décimo segundo mês": "2025-12"
    }

    for mes, valor in meses.items():
        if mes in comando:
            palavras_chave["mes"] = valor

    # Variáveis para método de pagamento
    metodos_pagamento = {
        "pix": "pix", "dinheiro": "dinheiro", "boleto": "boleto", 
        "cartão de crédito": "cartão de crédito", "cartão de débito": "cartão de débito", 
        "crédito": "cartão de crédito", "débito": "cartão de débito", 
        "no crédito": "cartão de crédito", "no débito": "cartão de débito", 
        "pagou no pix": "pix", "pagou em dinheiro": "dinheiro", 
        "transferência bancária": "pix", "pago com boleto": "boleto", 
        "boleto bancário": "boleto", "no cartão de crédito": "cartão de crédito", 
        "no cartão de débito": "cartão de débito", "cartão": "cartão de crédito"
    }

    for metodo, valor in metodos_pagamento.items():
        if metodo in comando:
            palavras_chave["metodo_pagamento"] = valor

    # Variáveis para categoria e descrição
    categorias_possiveis = [
        "alimentação", "serviços", "insumos", "suprimentos", 
        "fornecedores", "mercadorias", "combustível", "aluguel", 
        "manutenção", "limpeza", "transporte", "materiais", 
        "propaganda", "marketing", "publicidade", "impostos", 
        "compra de equipamentos", "equipamentos", "produtos", "predial", 
        "luz", "reparos"
    ]
    
    for categoria in categorias_possiveis:
        if categoria in comando:
            palavras_chave["categoria"] = categoria
            palavras_chave["detalhamento"] = "categoria"

    descricoes_possiveis = [
        "insumos", "material", "produtos", "estoque", 
        "ferramentas", "equipamentos", "papelaria", "informática", 
        "tecnologia", "software", "hardware", "peças", 
        "comida", "bebida", "suporte técnico", "consultoria", 
        "impostos", "predial", "luz", "reparos", "produtos"
    ]
    
    for descricao in descricoes_possiveis:
        if descricao in comando:
            palavras_chave["descricao"] = descricao
            palavras_chave["detalhamento"] = "descricao"

    # Se nenhum detalhamento específico for identificado, assumir relatório mensal total
    if palavras_chave["detalhamento"] is None:
        palavras_chave["detalhamento"] = "mensal_total"

    return palavras_chave

# Função para gerar o relatório com base nas palavras-chave extraídas
def gerar_relatorio(df, tipo_transacao=None, categoria=None, descricao=None, metodo_pagamento=None):
    # Aplicar filtros conforme solicitado
    if tipo_transacao and tipo_transacao != 'completo':
        df = df[df['Tipo de Transação'] == tipo_transacao]
    
    if categoria:
        df = df[df['Categoria'] == categoria]
    
    if descricao:
        df = df[df['Descrição'] == descricao]
    
    if metodo_pagamento:
        df = df[df['Método de Pagamento'] == metodo_pagamento]
    
    # Calcular total
    total = df['Valor (R$)'].sum()
    return total, df

# Carregar as planilhas conforme o código original
caminho_pasta = r'C:\Users\jadso\Desktop\AssistenteIA'
caminho_reports = os.path.join(caminho_pasta, 'reports')
if not os.path.exists(caminho_reports):
    os.makedirs(caminho_reports)

arquivos_excel = glob(os.path.join(caminho_pasta, 'Planilha seu francisco - FAST FOOD - *.xlsx'))
dataframes = []

for arquivo in arquivos_excel:
    try:
        df = pd.read_excel(arquivo)
        df = df[pd.to_datetime(df['Data'], errors='coerce').notna()]
        df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
        df['Mês'] = df['Data'].dt.strftime('%Y-%m')
        df['Tipo de Transação'] = df['Tipo de Transação'].str.lower()
        df['Categoria'] = df['Categoria'].str.lower()
        df['Descrição'] = df['Descrição'].str.lower()
        df['Método de Pagamento'] = df['Método de Pagamento'].str.lower()
        dataframes.append(df)
        print(f"Arquivo {os.path.basename(arquivo)} carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar {os.path.basename(arquivo)}: {e}")

if dataframes:
    df_combined = pd.concat(dataframes, ignore_index=True)
    print("Todos os arquivos foram combinados com sucesso.")
else:
    print("Nenhum arquivo foi carregado. Verifique o caminho e os arquivos disponíveis.")
    exit()

# Solicitar ao usuário que insira um comando
while True:
    comando_usuario = input("Digite o comando para gerar um relatório personalizado: ")
    filtros = interpretar_comando(comando_usuario)

    if filtros["cancelar"]:
        print("Operação cancelada. Retornando ao menu principal.")
        break

    if not filtros["tipo_transacao"]:
        print("Não foi possível identificar o tipo de transação (recebimento, pagamento ou completo). Tente novamente.")
        continue

    if not filtros["mes"]:
        print("Não foi possível identificar o mês desejado. Tente novamente.")
        continue

    total, df_detalhado = gerar_relatorio(
        df_combined,
        tipo_transacao=filtros["tipo_transacao"],
        categoria=filtros["categoria"],
        descricao=filtros["descricao"],
        metodo_pagamento=filtros["metodo_pagamento"]
    )

    if df_detalhado.empty:
        print("Nenhum registro encontrado com os filtros especificados.")
    else:
        print(f"Total {filtros['tipo_transacao']} no mês {filtros['mes']}: R${total:.2f}")
        print(df_detalhado)

        # Salvar os resultados em um arquivo Excel
        detalhes = f'_{filtros["detalhamento"]}' if filtros["detalhamento"] != "mensal_total" else ""
        relatorio_nome = f'relatorio_{filtros["tipo_transacao"]}_{filtros["mes"]}{detalhes}.xlsx'
        df_detalhado.to_excel(os.path.join(caminho_reports, relatorio_nome), index=False)
        print(f"Relatório salvo como {relatorio_nome} na pasta 'reports'.")
        break
