## 📊 Análise de Logs FortiGate

Projeto em Python para processar e analisar arquivos de logs gerados por firewalls FortiGate numa empresa, com o objetivo de identificar **inconsistências**, **padrões suspeitos** e gerar **estatísticas e visualizações** que apoiem a **tomada de decisões em cibersegurança**.

---

### 🧩 Funcionalidades Principais

- **Leitura de logs**  
  Suporte a logs de tráfego, eventos e segurança exportados do FortiGate ou FortiAnalyzer.

- **Análise de inconsistências**  
  - Detecção de sessões duplicadas.  
  - Identificação de IPs inesperados.  
  - Verificação de falhas na geração de logs ou registros truncados.

- **Métricas de uso**  
  - IPs mais ativos (origem e destino).  
  - Protocolos e serviços mais utilizados.  
  - Volume de dados transmitidos por IP, porta ou protocolo.  
  - Distribuição temporal de eventos (picos de tráfego, padrões horários).

- **Geração de relatórios e gráficos**  
  - Apresentação dos dados de forma clara no terminal e exportação para arquivos (CSV, JSON).  
  - Geração de **gráficos personalizados que facilitam a visualização dos fluxos de tráfego permitidos por cada política de firewall**.  
  - Esses gráficos apoiam a **identificação de anomalias**, como acessos fora do padrão, e são especialmente úteis para detectar **políticas mal configuradas**, incluindo:
    - Políticas com `Service: ALL`  
    - Políticas com `Source` ou `Destination: ANY`  
    - Regras com escopos excessivamente amplos que prejudicam a segurança
