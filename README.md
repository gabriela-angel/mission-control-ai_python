# Mission Control AI

Durante uma missão espacial, diferentes informações precisam ser analisadas continuamente, como temperatura, comunicação, bateria, oxigênio e estabilidade operacional. A partir desses dados, criamos um sistema de monitoramento e análise de missões espaciais desenvolvido em Python. Processa dados de telemetria de múltiplos ciclos, classifica riscos em tempo real e gera relatórios completos de missão.

---

## 👥 Equipe

 -   Gabriela Angel Silva - RM 570808
 -   Izabelly Menezes - RM 570673
 -   Marcos Paulo Sampaio - RM 573987

---

## 📋 Visão Geral

O **Mission Control AI** analisa cinco áreas críticas de uma missão a cada ciclo de operação:

| Área | Unidade |
|------|---------|
| Temperatura interna | °C |
| Comunicação com a base | % |
| Sistema de energia (bateria) | % |
| Suporte de oxigênio | % |
| Estabilidade operacional | % |

Para cada área, o sistema atribui uma pontuação de risco e classifica o ciclo como **ESTÁVEL**, **EM ATENÇÃO** ou **CRÍTICA**, gerando recomendações automáticas de ação.

---

## 🗂️ Estrutura do Código

```
mission_control.py
├── Macros / Configurações
├── Variáveis Globais
│   ├── dados_missao       # Matriz de leituras por ciclo
│   ├── areas_monitoradas  # Nomes das áreas
│   ├── alert_state        # Rótulos de estado (NORMAL, ATENÇÃO, CRÍTICO)
│   ├── alert_msg          # Mensagens de alerta por área
│   └── risk_points        # Pontuações de risco por ciclo
└── Funções
    ├── analyze_temperature()
    ├── analyze_communication()
    ├── analyze_battery()
    ├── analyze_oxygen()
    ├── analyze_stability()
    ├── classify_mission_cycle()
    ├── analyze_tendency()
    ├── cycle_report()
    ├── final_report()
    └── mission_report()
```

---

## ⚙️ Lógica de Classificação de Risco

Cada área retorna uma pontuação de **0** (normal), **1** (atenção) ou **2** (crítico):

### 🌡️ Temperatura
| Condição | Pontuação |
|----------|-----------|
| < 18 °C | 1 — Abaixo do ideal |
| 18–30 °C | 0 — Estável |
| 31–35 °C | 1 — Elevada |
| > 35 °C | 2 — Risco de superaquecimento |

### 📡 Comunicação
| Condição | Pontuação |
|----------|-----------|
| ≥ 60% | 0 — Estável |
| 30–59% | 1 — Instável |
| < 30% | 2 — Crítica |

### 🔋 Bateria
| Condição | Pontuação |
|----------|-----------|
| ≥ 50% | 0 — Estável |
| 20–49% | 1 — Abaixo do recomendado |
| < 20% | 2 — Crítica |

### 🫁 Oxigênio
| Condição | Pontuação |
|----------|-----------|
| ≥ 90% | 0 — Adequado |
| 80–89% | 1 — Abaixo do ideal |
| < 80% | 2 — Crítico |

### ⚖️ Estabilidade
| Condição | Pontuação |
|----------|-----------|
| ≥ 70% | 0 — Adequada |
| 40–69% | 1 — Reduzida |
| < 40% | 2 — Crítica |

---

## 🚦 Classificação do Ciclo

A soma das pontuações de risco do ciclo determina sua classificação:

| Soma de Pontos | Classificação |
|----------------|---------------|
| 0–2 | ✅ MISSÃO ESTÁVEL |
| 3–5 | ⚠️ MISSÃO EM ATENÇÃO |
| 6–10 | 🚨 MISSÃO CRÍTICA |

### Recomendações Automáticas

O sistema identifica a área de maior prioridade e emite uma recomendação:

- Múltiplas áreas críticas → *"Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."*
- Uma área crítica → Recomendação específica para aquela área
- Múltiplas áreas em atenção → *"Monitorar sistemas em atenção e preparar plano de contingência."*
- Operação normal → *"Manter operação normal e continuar monitoramento."*

---

## 📊 Saída do Sistema

### Relatório por Ciclo (`cycle_report`)
Para cada ciclo, exibe:
- Leituras de todas as 5 áreas com estado e mensagem de alerta
- Pontuação de risco total do ciclo
- Classificação e recomendação

### Relatório Final (`final_report`)
Ao final de todos os ciclos, exibe:
- Médias de cada área monitorada
- Ciclo mais crítico e maior pontuação de risco
- Risco médio da missão e quantidade de ciclos críticos
- Tendência geral da missão (melhora / piora / estável)
- Pontuação acumulada por área e área mais afetada
- Classificação final da missão

---

## 🚀 Como Executar

**Pré-requisito:** Python 3.6+

```bash
python mission_control.py
```

Nenhuma dependência externa é necessária.

---

## ✏️ Como Personalizar

### Alterar missão ou equipe
```python
MISSION_NAME = "Nome da Sua Missão"
TEAM_NAME    = "Nome da Sua Equipe"
```

### Adicionar ou modificar ciclos
Edite a matriz `dados_missao`. Cada linha representa um ciclo com 5 valores na ordem:
```
[Temperatura(°C), Comunicação(%), Bateria(%), Oxigênio(%), Estabilidade(%)]
```

Exemplo:
```python
dados_missao = [
    [24, 92, 88, 96, 90],  # Ciclo 1
    [27, 80, 72, 94, 85],  # Ciclo 2
    # ...
]
```

---

## 🛰️ Exemplo de Saída

```
============================================================
MISSION CONTROL AI
============================================================
Missão: Sirius Test Alpha
Equipe: Equipe Acrux
Quantidade de ciclos analisados: 1
============================================================

CICLO 1
------------------------------------------------------------
Temperatura: 24 °C | NORMAL | Temperatura estável
Comunicação: 92% | NORMAL | Comunicação estável
Bateria: 88% | NORMAL | Energia estável
Oxigênio: 96% | NORMAL | Oxigênio adequado
Estabilidade: 90% | NORMAL | Estabilidade operacional adequada
Pontuação de risco do ciclo: 0
Classificação do ciclo: MISSÃO ESTÁVEL
Recomendação: Manter operação normal e continuar monitoramento.

============================================================
RELATÓRIO FINAL DA MISSÃO
============================================================
Missão: Sirius Test Alpha
Equipe: Equipe Acrux

Quantidade de ciclos analisados: 1

Média de temperatura: 24.00 °C
Média de comunicação: 92.00%
Média de bateria: 88.00%
Média de oxigênio: 96.00%
Média de estabilidade: 90.00%

Ciclo mais crítico: Ciclo 1
Maior pontuação de risco: 0
Risco médio da missão: 0.00
Quantidade de ciclos críticos: 0

Tendência da missão:
A missão permaneceu estável em relação ao início.

Pontuação acumulada por área:
Temperatura interna: 0 pontos
Comunicação com a base: 0 pontos
Sistema de energia: 0 pontos
Suporte de oxigênio: 0 pontos
Estabilidade operacional: 0 pontos

Área mais afetada:
Temperatura interna

Classificação final da missão:
MISSÃO ESTÁVEL
```