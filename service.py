import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estética dos gráficos
sns.set(style="whitegrid")

# Dicionário de portas conhecidas
PORT_SERVICE_MAP = {
  1: "ICMP",
  6: "TCP",
  17: "UDP",
  47: "GRE",
  50: "ESP",
  51: "AH",
  58: "ICMPv6",
  89: "OSPF",
  8090: "Web",
  8000: "Web",
  5432: "PostgreSQL",
  3389: "RDP",
  445: "SMB",
  443: "HTTPS",
  389: "LDAP",
  135: "RPC",
  123: "NTP",
  111: "RCP",
  53: "DNS",
  22: "SSH",
  80: "HTTP",
  161: "SNMP",
  3299: "Porta 3299",
  2049: "NFS SERVER",
  3389: "RDP Microsoft Terminal Server",
  3306: "MySQL",
  8080: "HTTP",
  6568: "Porta 6568",
  6443: "Kubernetes API"
}

def get_service_name(port):
    try:
        return PORT_SERVICE_MAP.get(int(port), f"Porta ({port})")
    except:
        return f"(Não usa porta)"

# Carrega o CSV
df = pd.read_csv('129.csv')

# Aplica o mapeamento
df['service_name'] = df['protocol'].apply(get_service_name)

# Conta quantas vezes cada serviço apareceu
service_counts = df['service_name'].value_counts().sort_values(ascending=False)

# Gera gráfico
plt.figure(figsize=(12, 6))
sns.barplot(x=service_counts.values, y=service_counts.index, palette="viridis")
plt.title("Frequência dos Serviços Baseados nas Portas")
plt.xlabel("Número de Registros")
plt.ylabel("Serviço")
plt.tight_layout()
plt.show()
