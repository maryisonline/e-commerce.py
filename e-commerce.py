# 1
# import do kaggle (eu pego diretamente do site no dataset que eu escolher, o codigo vme pronto pra importar)
import kagglehub

# Download latest version
path = kagglehub.dataset_download("uom190346a/e-commerce-customer-behavior-dataset")

print("Path to dataset files:", path)

# 2
# aqui faço um import do sistema operacional pra verificar se o dataset correto foi baixado
import os

print("Arquivos baixados:", os.listdir(path))

# 3
# pra ler as primeira infos do arquivo e eu poder identificar o tipo de dado
import pandas as pd
import matplotlib as plt
import seaborn as sns

# definindo q o arquivo em questao esta o caminho do path q defini anteriormente (eu pego o nome do arquivo dps q valido se ele foi baixado pq o terminal me retorna ele com o print)
file = os.path.join(path, "E-commerce Customer Behavior - Sheet1.csv")

# o df (dataframe) eh pra ler o arquivo, so assim eu vou conseguir trazer as informacoes dele. é literalmente como se o pd.read fosse abrir o livro e o resto fosse a ação de ler 
df = pd.read_csv(file)
print(df.head()) # le as primeiras linhas
print(df.info()) # le o tipo de dados
print(df.describe()) # estatisticas basicas

# 4
# o streamlit vai permitir q eu visualize esse dashboard localmente
# import streamlit as st

# st.title("Customer Behavior - Dashboard")
# st.write("Dados analisados:")
# st.dataframe(df.head())

from dash import Dash, dcc, html
import plotly.graph_objects as go

app = Dash(__name__)

fig = go.Figure(data=[go.Bar(x=df['Gender'], y=df['Total Spend'])])

app.layout = html.Div([
    html.H1("Dashboard Kaggle"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
