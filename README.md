## Finalidade dos Códigos

### 1. Código de Visualização Sankey (`map_protocolo_and_porta.py.py`)

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
