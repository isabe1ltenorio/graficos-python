## Finalidade dos Códigos

### 1. Código de Visualização Sankey (`map_protocolo_and_porta.py`)

**Para que serve:**  
Cria diagramas de fluxo interativos (Sankey) para analisar como o tráfego de rede se move através das políticas de firewall do FortiGate, mostrando:
- **Conexões** entre portas de origem → protocolos → portas de destino
- **Padrões** de tráfego frequentes
- **Serviços** mais utilizados (HTTP, SSH, RDP, etc.)

**Principais aplicações:**  
- Identificar políticas de firewall pouco eficientes  
- Visualizar concentração de tráfego em portas específicas  
- Detectar protocolos incomuns ou não autorizados  

---

### 2. Código Divisor de CSV (`dividir-csv.py`)

**Para que serve:**  
Divide arquivos grandes de logs do FortiGate em partes menores para:
- Facilitar processamento e gerar gráficos mais compreensíveis  
- Permitir análise paralela de diferentes segmentos  
- Contornar limitações de ferramentas que não lidam bem com arquivos muito grandes  

**Principais aplicações:**  
- Pré-processamento de logs antes da análise  
- Preparação de dados para processamento distribuído  
- Divisão de capturas longas para envio por sistemas com limitação de tamanho  

---

### 3. Código de Distribuição de IPs de Origem (`ip.py`)

**Para que serve:**  
Gera um gráfico de pizza mostrando a frequência de requisições por IP de origem, com porcentagem e legenda detalhada.

**Principais aplicações:**  
- Identificar os principais emissores de tráfego  
- Avaliar concentração de acessos em determinados IPs  
- Detectar fontes suspeitas com alto volume de conexões  

---

### 4. Código de Frequência dos Serviços por Portas (`service.py`)

**Para que serve:**  
Agrupa os registros por porta e traduz para o nome do serviço correspondente (ex: 443 → HTTPS), exibindo um gráfico de barras com as ocorrências de cada serviço.

**Principais aplicações:**  
- Entender quais serviços são mais utilizados no ambiente  
- Auxiliar na priorização de políticas de segurança por criticidade de uso  
- Identificar portas não padronizadas com alto tráfego  

---

### 5. Código de Classificação das Portas de Origem e Destino (`source.py`)

**Para que serve:**  
Classifica as portas de origem dos acessos em:
- Serviços conhecidos (SSH, HTTP, etc.)
- Faixas de valor (ex: 0–10k, 10k–20k)
- Outras categorias como “Acima de 100k” ou “Não usa porta”

Exibe a distribuição em um gráfico de pizza com legenda lateral.

**Principais aplicações:**  
- Observar padrões de variação em portas dinâmicas  
- Identificar possíveis anomalias ou uso incomum de portas  
- Compreender a dispersão dos acessos em relação ao uso de portas específicas  
