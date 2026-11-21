import pandas as pd
import numpy as np

# Configurar a semente para gerar sempre os mesmos dados
np.random.seed(42)
num_entregas = 300

# Simular coordenadas em torno de uma região central (ex: São Paulo/Sudeste)
lat_base = -23.5505
lon_base = -46.6333

dados = {
    'id_pedido': [f"TRP-{1000+i}" for i in range(num_entregas)],
    'latitude': np.random.normal(lat_base, 1.5, num_entregas),
    'longitude': np.random.normal(lon_base, 1.5, num_entregas),
    'custo_frete': np.random.uniform(50, 400, num_entregas).round(2),
    'distancia_km': np.random.uniform(20, 600, num_entregas).round(1),
    'status_entrega': np.random.choice(['No Prazo', 'Atrasado'], num_entregas, p=[0.82, 0.18]) # 18% de atrasos
}

df = pd.DataFrame(dados)

# Criar um indicador chave de performance (KPI): Custo por Quilómetro
df['custo_por_km'] = (df['custo_frete'] / df['distancia_km']).round(2)

# Exportar para CSV
df.to_csv('dados_rotas.csv', index=False)
print("Base de dados 'dados_rotas.csv' gerada com sucesso!")