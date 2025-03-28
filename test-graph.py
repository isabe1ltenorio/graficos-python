import pandas as pd
import plotly.graph_objects as go

port_map = {
    "50000": "Personalizada",
    "49684": "Personalizada",
    "49676": "Personalizada",
    "44300": "Personalizada",
    "30441": "Personalizada",
    "30241": "Personalizada",
    "8090": "Web",
    "8000": "Web",
    "5432": "PostgreSQL",
    "3389": "RDP",
    "3300": "Personalizada",
    "3200": "Personalizada",
    "445": "SMB",
    "443": "HTTPS",
    "389": "LDAP",
    "135": "RPC",
    "123": "NTP",
    "111": "RCP",
    "53": "DNS" ,
    "22": "SSH",
    "3300": "Personalizada",
    "80": "HTTP",
    "3544": "Personalizada",
    "65444": "Personalizada",
    "161": "SNMP",
    "3299": "Personalizada",
    "2049": "NFS SERVER",
    "3389": "RDP Microsoft Terminal Server",
    "49178": "Personalizada",
    "50381": "Personalizada",
    "50986": "Personalizada",
    "51917": "Personalizada",
    "52245": "Personalizada",
    "52366": "Personalizada",
    "55287": "Personalizada",
    "62334": "Personalizada",
    "62638": "Personalizada",
    "62985": "Personalizada",
    "63819": "Personalizada",
    "3306": "MySQL",
    "123": "NTP",
    "3289:": "Personalizada",
    "8080": "HTTP",
    "6568": "Personalizada",
}


df = pd.read_csv("46-part_1.csv")  


df["source_port"] = df["source_port"].astype(str).map(lambda x: port_map.get(x, x))
df["destination_port"] = df["destination_port"].astype(str).map(lambda x: port_map.get(x, x))


nodes = list(set(df["source_port"]).union(set(df["destination_port"])))  
node_map = {node: i for i, node in enumerate(nodes)}  


sources = df["source_port"].map(node_map).tolist()
targets = df["destination_port"].map(node_map).tolist()
values = [1] * len(df)  


fig = go.Figure(go.Sankey(
    node=dict(
        pad=15, thickness=20, line=dict(color="black", width=0.1),
        label=nodes  
    ),
    link=dict(
        source=sources,  
        target=targets,  
        value=values  
    )
))


fig.update_layout(title_text="Regra de Firewall Nº 29", font_size=12)
fig.show()
