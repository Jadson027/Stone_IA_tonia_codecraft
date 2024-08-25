import pandas as pd
import os
from glob import glob

# Definir o caminho da pasta onde estão as planilhas
caminho_pasta = r'C:\Users\jadso\Desktop\AssistenteIA'

# Criar a pasta 'reports' se ela não existir
caminho_reports = os.path.join(caminho_pasta, 'reports')
if not os.path.exists(caminho_reports):
    os.makedirs(caminho_reports)

# Obter a lista de todos os arquivos Excel na pasta que correspondem ao padrão
arquivos_excel = glob(os.path.join(caminho_pasta, 'Planilha seu francisco - FAST FOOD - *.xlsx'))

# Lista para armazenar os DataFrames de cada arquivo
dataframes = []

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
        print(f"Arquivo {os.path.basename(arquivo)} carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar {os.path.basename(arquivo)}: {e}")

# Concatenar todos os DataFrames em um único
if dataframes:
    df_combined = pd.concat(dataframes, ignore_index=True)
    print("Todos os arquivos foram combinados com sucesso.")
else:
    print("Nenhum arquivo foi carregado. Verifique o caminho e os arquivos disponíveis.")
    exit()

# Solicitar ao usuário que insira o mês que deseja filtrar
meses_disponiveis = df_combined['Mês'].unique()
print("\nMeses disponíveis:")
for idx, mes in enumerate(meses_disponiveis, start=1):
    print(f"{idx}. {mes}")

mes_opcao = int(input("Selecione o número do mês que deseja filtrar: "))
mes_especifico = meses_disponiveis[mes_opcao - 1]

# Filtrar o DataFrame combinado pelo mês especificado
df_filtrado = df_combined[df_combined['Mês'] == mes_especifico].copy()

if df_filtrado.empty:
    print(f"Não há dados disponíveis para o mês {mes_especifico}.")
else:
    # Menu para escolha entre recebimentos, pagamentos ou ambos
    print("\nEscolha o tipo de transação:")
    print("1. Relatório de Recebimentos")
    print("2. Relatório de Pagamentos")
    print("3. Relatório Total Mensal Completo (Recebimentos + Pagamentos)")
    tipo_opcao = int(input("Digite o número da opção desejada: "))

    if tipo_opcao == 1:
        tipo_transacao = 'recebimento'
        df_filtrado = df_filtrado[df_filtrado['Tipo de Transação'] == tipo_transacao]
    elif tipo_opcao == 2:
        tipo_transacao = 'pagamento'
        df_filtrado = df_filtrado[df_filtrado['Tipo de Transação'] == tipo_transacao]
    elif tipo_opcao == 3:
        tipo_transacao = 'completo'
        # Não filtra por tipo de transação, para incluir ambos
    else:
        print("Opção inválida. Tente novamente.")
        exit()

    # Função para aplicar filtros e calcular resultados
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
    
    # Menu para escolha de detalhamento do relatório
    print("\nEscolha o detalhamento do relatório:")
    print("1. Relatório Mensal Total")
    print("2. Registros por Método de Pagamento (PIX, Boleto, etc.)")
    print("3. Registros por Categoria")
    print("4. Registros por Descrição")
    detalhamento_opcao = int(input("Digite o número da opção desejada: "))

    if detalhamento_opcao == 1:
        # Relatório Mensal Total
        total, df_detalhado = gerar_relatorio(df_filtrado)
        print(f"Total {tipo_transacao} no mês {mes_especifico}: R${total:.2f}")
    
    elif detalhamento_opcao == 2:
        # Menu de Métodos de Pagamento disponíveis
        metodos_disponiveis = df_filtrado['Método de Pagamento'].unique()
        print("\nMétodos de pagamento disponíveis:")
        for idx, metodo in enumerate(metodos_disponiveis, start=1):
            print(f"{idx}. {metodo}")
        
        metodo_opcao = int(input("Selecione o número do método de pagamento: "))
        metodo_pagamento = metodos_disponiveis[metodo_opcao - 1]
        
        total, df_detalhado = gerar_relatorio(df_filtrado, metodo_pagamento=metodo_pagamento)
        print(f"Total {tipo_transacao} no mês {mes_especifico} via {metodo_pagamento}: R${total:.2f}")
    
    elif detalhamento_opcao == 3:
        # Menu de Categorias disponíveis
        categorias_disponiveis = df_filtrado['Categoria'].unique()
        print("\nCategorias disponíveis:")
        for idx, categoria in enumerate(categorias_disponiveis, start=1):
            print(f"{idx}. {categoria}")
        
        categoria_opcao = int(input("Selecione o número da categoria: "))
        categoria = categorias_disponiveis[categoria_opcao - 1]
        
        total, df_detalhado = gerar_relatorio(df_filtrado, categoria=categoria)
        print(f"Total {tipo_transacao} na categoria {categoria} no mês {mes_especifico}: R${total:.2f}")
    
    elif detalhamento_opcao == 4:
        # Menu de Descrições disponíveis
        descricoes_disponiveis = df_filtrado['Descrição'].unique()
        print("\nDescrições disponíveis:")
        for idx, descricao in enumerate(descricoes_disponiveis, start=1):
            print(f"{idx}. {descricao}")
        
        descricao_opcao = int(input("Selecione o número da descrição: "))
        descricao = descricoes_disponiveis[descricao_opcao - 1]
        
        total, df_detalhado = gerar_relatorio(df_filtrado, descricao=descricao)
        print(f"Total {tipo_transacao} na descrição {descricao} no mês {mes_especifico}: R${total:.2f}")
    
    else:
        print("Opção inválida. Tente novamente.")

    # Exibir os detalhes do DataFrame na conversa
    print("\nResumo do Relatório:")
    print(df_detalhado)
    
    # Salvar os resultados em um arquivo Excel
    df_detalhado.to_excel(os.path.join(caminho_reports, f'relatorio_personalizado_{tipo_transacao}_{mes_especifico}.xlsx'), index=False)
    print(f"\nRelatório para {tipo_transacao} no mês {mes_especifico} foi salvo na pasta 'reports'.")
