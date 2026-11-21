# 📍 Dashboard de Análise de Fretes e Rotas (Otimização Logística)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](COLE_AQUI_O_SEU_LINK_DO_STREAMLIT_DEPOIS)

Este projeto é um painel interativo desenvolvido para o setor de **Logística e Transportes**. O objetivo principal é analisar os custos de frete, mapear as rotas de entrega e identificar ineficiências na operação, ajudando na tomada de decisão para redução de custos.

## 🎯 Problema de Negócio Resolvido
O transporte é geralmente o maior centro de custos de uma operação logística. Este dashboard permite aos analistas e gestores:
* Visualizar geograficamente onde estão os fretes mais caros.
* Monitorizar a taxa de atraso (OTIF) das entregas.
* Analisar a correlação entre a distância percorrida e o custo cobrado através de regressão linear (OLS).

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem principal)
* **Pandas & NumPy** (Manipulação e Análise de Dados)
* **Plotly** (Visualização de dados e Mapas Geoespaciais)
* **Streamlit** (Criação do Dashboard Web interativo)
* **Statsmodels** (Cálculo de tendências matemáticas)

## 💡 Principais Funcionalidades
1. **Mapeamento Geoespacial:** Mapa interativo que destaca visualmente o cumprimento dos prazos (cores) e o custo do frete (tamanho das bolhas).
2. **KPIs em Tempo Real:** Cálculo automático de Custo Total, Custo Médio por Km e Taxa de Atrasos.
3. **Filtros Dinâmicos:** Possibilidade de isolar na análise apenas as entregas atrasadas ou no prazo.

## 🚀 Como Executar o Projeto Localmente

1. Clone este repositório:
```bash
git clone [https://github.com/FernandoLouzada17/analise-rotas-logistica.git](https://github.com/FernandoLouzada17/analise-rotas-logistica.git)
cd analise-rotas-logistica