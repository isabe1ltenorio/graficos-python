import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo e tamanho global da fonte
sns.set(style="whitegrid")
plt.rcParams.update({
    'font.size': 10,           # Tamanho base
    'axes.titlesize': 12,      # Título dos gráficos
    'axes.labelsize': 12,      # Labels dos eixos
    'legend.fontsize': 8,     # Itens da legenda
    'legend.title_fontsize': 12  # Título da legenda
})

# Carregar dados
df = pd.read_csv('96.csv')

# Contagem por IP de origem
protocol_distribution = df['source_ip'].value_counts()
labels = protocol_distribution.index
sizes = protocol_distribution.values

# Criar legenda personalizada com porcentagem
percentages = [f'{label} - {value / sizes.sum() * 100:.1f}%' for label, value in zip(labels, sizes)]

# Plotar gráfico
plt.figure(figsize=(8, 8))
plt.pie(sizes, startangle=140)
plt.title('Distribuição dos IPs de Origem')

# Adicionar legenda ao lado com títulos
plt.legend(percentages, title="IPs de Origem", loc="center left", bbox_to_anchor=(1, 0.5))

# Ajustar layout para não cortar a legenda
plt.tight_layout()
plt.show()
