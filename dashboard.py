import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import os
from glob import glob

# Carregar os dados das planilhas
caminho_pasta = r'C:\Users\jadso\Desktop\AssistenteIA'

arquivos_excel = glob(os.path.join(caminho_pasta, 'Planilha seu francisco - FAST FOOD - *.xlsx'))
dataframes = []

for arquivo in arquivos_excel:
    try:
        df = pd.read_excel(arquivo)
        df = df[pd.to_datetime(df['Data'], errors='coerce').notna()]
        df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
        df['Mês'] = df['Data'].dt.to_period('M')  # Formatar as datas como períodos mensais
        
        # Padronizar colunas de texto para minúsculas
        df['Tipo de Transação'] = df['Tipo de Transação'].str.lower()
        df['Categoria'] = df['Categoria'].str.lower()
        df['Descrição'] = df['Descrição'].str.lower()
        df['Método de Pagamento'] = df['Método de Pagamento'].str.lower()
        
        dataframes.append(df)
    except Exception as e:
        print(f"Erro ao carregar {os.path.basename(arquivo)}: {e}")

if dataframes:
    df_combined = pd.concat(dataframes, ignore_index=True)
else:
    print("Nenhum arquivo foi carregado. Verifique o caminho e os arquivos disponíveis.")
    exit()

# Criação do Dashboard usando Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Teste Básico de Gráfico", style={'textAlign': 'center'}),
    
    # Dropdown para selecionar o mês
    dcc.Dropdown(
        id='mes-dropdown',
        options=[{'label': str(mes), 'value': str(mes)} for mes in df_combined['Mês'].unique()],
        value=str(df_combined['Mês'].unique()[0]),  # Seleciona o primeiro mês como padrão
        clearable=False,
        style={'margin-bottom': '20px'}
    ),
    
    # Gráfico Simples
    dcc.Graph(id='grafico-simples')
])

@app.callback(
    Output('grafico-simples', 'figure'),
    [Input('mes-dropdown', 'value')]
)
def update_grafico(mes_selecionado):
    df_filtrado = df_combined[df_combined['Mês'].astype(str) == mes_selecionado]
    
    # Gráfico simples de barras
    fig = px.bar(df_filtrado, x='Categoria', y='Valor (R$)', color='Tipo de Transação',
                 title=f'Gráfico de Barras para {mes_selecionado}')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
