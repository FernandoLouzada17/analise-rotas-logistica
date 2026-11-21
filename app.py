import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da Página
st.set_page_config(page_title="Otimização de Rotas", layout="wide")
st.title("📍 Dashboard de Análise de Fretes e Rotas")
st.markdown("Identifique gargalos de transporte e custos elevados na operação logística através de dados geoespaciais.")

# 2. Carregar Dados
@st.cache_data
def carregar_dados():
    return pd.read_csv('dados_rotas.csv')

df = carregar_dados()

# 3. Filtros Laterais
st.sidebar.header("Filtros de Operação")
status_filtro = st.sidebar.multiselect(
    "Filtrar por Status de Entrega:",
    options=df['status_entrega'].unique(),
    default=df['status_entrega'].unique()
)

df_filtrado = df[df['status_entrega'].isin(status_filtro)]

# 4. KPIs (Indicadores Chave)
st.subheader("📊 Visão Geral da Operação")
col1, col2, col3, col4 = st.columns(4)

total_entregas = len(df_filtrado)
if total_entregas > 0:
    custo_total = df_filtrado['custo_frete'].sum()
    custo_medio_km = df_filtrado['custo_por_km'].mean()
    entregas_atrasadas = len(df_filtrado[df_filtrado['status_entrega'] == 'Atrasado'])
    taxa_atraso = (entregas_atrasadas / total_entregas) * 100
else:
    custo_total = custo_medio_km = taxa_atraso = 0

col1.metric("Total de Entregas", f"{total_entregas}")
col2.metric("Custo Total de Frete", f"R$ {custo_total:,.2f}")
col3.metric("Custo Médio por Km", f"R$ {custo_medio_km:.2f}")
col4.metric("Taxa de Atraso", f"{taxa_atraso:.1f}%")

# 5. Mapa Interativo Geoespacial
st.subheader("🗺️ Mapeamento de Entregas")
st.markdown("Os pontos maiores representam fretes mais caros. As cores indicam o cumprimento do prazo.")

fig_mapa = px.scatter_map(
    df_filtrado, 
    lat="latitude", 
    lon="longitude", 
    color="status_entrega",
    size="custo_frete",
    hover_name="id_pedido",
    hover_data={"custo_por_km": True, "distancia_km": True, "latitude": False, "longitude": False},
    color_discrete_map={"No Prazo": "green", "Atrasado": "red"},
    zoom=5, 
    map_style="carto-positron"
)
st.plotly_chart(fig_mapa, use_container_width=True)

# 6. Gráfico de Dispersão
st.subheader("📈 Análise de Eficiência (Custo vs Distância)")
fig_grafico = px.scatter(
    df_filtrado, 
    x="distancia_km", 
    y="custo_frete", 
    color="status_entrega",
    trendline="ols",
    title="Relação entre Distância Percorrida e Custo do Frete"
)
st.plotly_chart(fig_grafico, use_container_width=True)