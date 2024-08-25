import pandas as pd
import os
from glob import glob

# Definir os caminhos das planilhas
caminho_pasta = r'C:\Users\jadso\Desktop\AssistenteIA'
arquivos_excel = [
    os.path.join(caminho_pasta, 'Planilha seu francisco - FAST FOOD - Janeiro.xlsx'),
    os.path.join(caminho_pasta, 'Planilha seu francisco - FAST FOOD - Fevereiro.xlsx'),
    os.path.join(caminho_pasta, 'Planilha seu francisco - FAST FOOD - Março.xlsx')
]

# Lista para armazenar os DataFrames de cada arquivo
dataframes = []
meses = []

# Loop através de cada arquivo e ler o conteúdo
for arquivo in arquivos_excel:
    try:
        df = pd.read_excel(arquivo)
        
        # Remover linhas que não contenham datas válidas na coluna 'Data'
        df = df[pd.to_datetime(df['Data'], errors='coerce').notna()]
        
        # Converter a coluna 'Data' para datetime
        df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
        
        # Extrair o mês e o ano da coluna 'Data' e criar uma nova coluna 'Mês'
        df['Mês'] = df['Data'].dt.strftime('%Y-%m')

        # Padronizar colunas de texto para minúsculas
        df['Tipo de Transação'] = df['Tipo de Transação'].str.lower()
        df['Categoria'] = df['Categoria'].str.lower()
        df['Descrição'] = df['Descrição'].str.lower()
        df['Método de Pagamento'] = df['Método de Pagamento'].str.lower()
        
        dataframes.append(df)
        meses.append(df['Mês'].unique()[0])
    except Exception as e:
        print(f"Erro ao carregar {os.path.basename(arquivo)}: {e}")

# Concatenar todos os DataFrames em um único DataFrame
if dataframes:
    df_combined = pd.concat(dataframes, ignore_index=True)
else:
    print("Nenhum arquivo foi carregado. Verifique o caminho e os arquivos disponíveis.")
    exit()

# Usar a coluna 'Valor (R$)' para cálculos financeiros
valor_coluna = 'Valor (R$)'

# Função para calcular o Lucro do Mês
def calcular_lucro(df):
    total_pagamentos = df[df['Tipo de Transação'] == 'pagamento'][valor_coluna].abs().sum()
    total_recebimentos = df[df['Tipo de Transação'] == 'recebimento'][valor_coluna].sum()
    lucro = total_recebimentos - total_pagamentos
    return total_pagamentos, total_recebimentos, lucro

# Função para calcular a Necessidade de Capital de Giro (NCG)
def calcular_ncg(df):
    # Contas a Pagar (CP): Todo pagamento na coluna 'Tipo de Transação'
    contas_a_pagar = df[df['Tipo de Transação'] == 'pagamento'][valor_coluna].abs().sum()

    # Contas a Receber (CR): Todos os recebimentos na coluna 'Tipo de Transação'
    contas_a_receber = df[df['Tipo de Transação'] == 'recebimento'][valor_coluna].sum()

    # Valor em Estoque (VE): 'Compra de insumos' na coluna 'Descrição'
    valor_estoque = df[df['Descrição'] == 'compra de insumos'][valor_coluna].sum()

    # Fórmula da NCG: CP – (CR + VE)
    ncg = contas_a_pagar - (contas_a_receber + valor_estoque)
    return ncg

# Função para prever o Capital de Giro necessário no próximo mês
def prever_capital_de_giro(lucros, vendas, gastos, capital_de_giro_atual):
    # Analisar as oscilações de vendas e gastos
    variacao_vendas = (max(vendas) - min(vendas)) / len(vendas) if len(vendas) > 1 else 0
    variacao_gastos = (max(gastos) - min(gastos)) / len(gastos) if len(gastos) > 1 else 0

    # Prever necessidade de capital de giro considerando oscilações e histórico
    previsao_gastos = sum(gastos) / len(gastos) + variacao_gastos
    previsao_vendas = sum(vendas) / len(vendas) - variacao_vendas

    # Previsão de capital de giro para o próximo mês
    previsao_capital_giro = capital_de_giro_atual + previsao_gastos - previsao_vendas
    return previsao_capital_giro

# Solicitar ao usuário qual opção ele deseja analisar
print("Opções disponíveis:")
for i, mes in enumerate(meses, start=1):
    print(f"{i}. {mes}")
print(f"{len(meses)+1}. Gerenciamento Total")
print(f"{len(meses)+2}. Previsibilidade Financeira")
opcao_escolhida = int(input("Digite o número da opção desejada: ").strip())

# Verificar a opção escolhida
if opcao_escolhida <= len(meses):
    mes_escolhido = meses[opcao_escolhida-1]
    df_mes = df_combined[df_combined['Mês'] == mes_escolhido]

    # Calcular valores para o mês escolhido
    total_pagamentos, total_recebimentos, lucro = calcular_lucro(df_mes)
    ncg = calcular_ncg(df_mes)

    # Exibir os resultados para o mês escolhido
    print(f"\n--- Resultados para {mes_escolhido} ---")
    print(f"Total de Pagamentos: R$ {total_pagamentos:.2f}")
    print(f"Total de Recebimentos: R$ {total_recebimentos:.2f}")
    print(f"Lucro do Mês: R$ {lucro:.2f}")
    print(f"Necessidade de Capital de Giro (NCG): R$ {ncg:.2f}")

elif opcao_escolhida == len(meses) + 1:
    # Gerenciamento Total
    total_pagamentos_geral = 0
    total_recebimentos_geral = 0
    lucro_acumulado = 0
    capital_de_giro_acumulado = 0

    for mes in meses:
        df_mes = df_combined[df_combined['Mês'] == mes]
        total_pagamentos, total_recebimentos, lucro = calcular_lucro(df_mes)
        ncg = calcular_ncg(df_mes)

        total_pagamentos_geral += total_pagamentos
        total_recebimentos_geral += total_recebimentos
        lucro_acumulado += lucro
        capital_de_giro_acumulado += lucro

    # Exibir os resultados para o gerenciamento total
    print("\n--- Resultados Gerenciamento Total ---")
    print(f"Total de Pagamentos: R$ {total_pagamentos_geral:.2f}")
    print(f"Total de Recebimentos: R$ {total_recebimentos_geral:.2f}")
    print(f"Lucro Total Acumulado: R$ {lucro_acumulado:.2f}")
    print(f"Capital de Giro Acumulado (Saldo): R$ {capital_de_giro_acumulado:.2f}")
    print(f"Necessidade de Capital de Giro (NCG): R$ {ncg:.2f}")

elif opcao_escolhida == len(meses) + 2:
    # Previsibilidade Financeira
    lucros = []
    vendas = []
    gastos = []
    capital_de_giro_atual = 0

    for mes in meses:
        df_mes = df_combined[df_combined['Mês'] == mes]
        total_pagamentos, total_recebimentos, lucro = calcular_lucro(df_mes)
        lucros.append(lucro)
        vendas.append(total_recebimentos)
        gastos.append(total_pagamentos)
        capital_de_giro_atual += lucro

    previsao_capital_giro = prever_capital_de_giro(lucros, vendas, gastos, capital_de_giro_atual)

    # Exibir os resultados da previsão financeira
    print("\n--- Previsibilidade Financeira ---")
    print(f"Previsão de Capital de Giro necessário para o próximo mês: R$ {previsao_capital_giro:.2f}")

else:
    print("Opção inválida. Tente novamente.")
