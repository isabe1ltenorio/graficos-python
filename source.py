import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Carrega o CSV
df = pd.read_csv('96.csv')

# Converte a coluna source_port para numérica
df['source_port'] = pd.to_numeric(df['source_ip'], errors='coerce')

# Dicionário de portas conhecidas
known_ports = {
    1: "ICMP", 6: "TCP", 17: "UDP", 47: "GRE", 50: "ESP", 51: "AH", 58: "ICMPv6", 89: "OSPF",
    22: "SSH", 53: "DNS", 80: "HTTP", 123: "NTP", 135: "RPC", 389: "LDAP", 443: "HTTPS",
    445: "SMB", 111: "RCP", 161: "SNMP", 2049: "NFS SERVER", 3299: "Porta 3299",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 6443: "Kubernetes API",
    6568: "Porta 6568", 8000: "Web", 8080: "HTTP", 8090: "Web"
}

# Função para classificar a porta
def classify_port(port):
    if pd.isna(port):
        return 'Não usa porta'
    port = int(port)
    if port in known_ports:
        return known_ports[port]
    elif port < 100000:
        faixa = f'{(port//10000)*10}k–{((port//10000)+1)*10}k'
        return faixa
    else:
        return 'Acima de 100k'

# Aplica a classificação
df['port_group'] = df['source_port'].apply(classify_port)

# Conta a distribuição por grupo
distribution = df['port_group'].value_counts().sort_index()

# Gera o gráfico com legenda ao lado
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    distribution,
    labels=None,  # sem rótulos nas fatias
    autopct='%1.1f%%',
    startangle=140
)

# Adiciona a legenda ao lado
ax.legend(
    wedges,
    distribution.index,
    title="Portas",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize='medium'
)

plt.title('Distribuição das portas de origem (nomes conhecidos + faixas)')
plt.tight_layout()
plt.show()
