# MACROS
MISSION_NAME = "Sirius Test Alpha"
TEAM_NAME = "Equipe Acrux"

# Indica o que cada coluna representa na matriz dados_missao
TEMPERATURE_COL = 0 # valor medido em °C
COMMUNICATION_COL = 1 # valor medido em %
BATTERY_COL = 2 # valor medido em %
OXYGEN_COL = 3 # valor medido em %
STABILITY_COL = 4 # valor medido em %

# GLOBAL VARIABLES
dados_missao = [
[24, 92, 88, 96, 90],
[27, 80, 72, 94, 85],
[31, 65, 58, 91, 70],
[36, 42, 38, 87, 55],
[39, 28, 19, 78, 35],
[34, 55, 32, 82, 50]
]

areas_monitoradas = [
"Temperatura interna",
"Comunicação com a base",
"Sistema de energia",
"Suporte de oxigênio",
"Estabilidade operacional"
]

alert_state = ["NORMAL", "ATENÇÃO", "CRÍTICO"]
alert_msg = [
["Temperatura estável", "Temperatura elevada", "Risco de superaquecimento", "Temperatura abaixo do ideal"],
["Comunicação estável", "Comunicação instável", "Comunicação com a base em nível crítico"],
["Energia estável", "Bateria abaixo do recomendado", "Bateria em nível crítico"],
["Oxigênio adequado", "Oxigênio abaixo do ideal", "Oxigênio em nível crítico"],
["Estabilidade operacional adequada", "Estabilidade operacional reduzida", "Estabilidade operacional crítica"]
]

risk_points = [] # armazena a pontuacao de risco por categoria por ciclo

# FUNCTIONS
def analyze_temperature(temp):
    if temp < 18:
        return 1
    elif temp <= 30:
        return 0
    elif temp <= 35:
        return 1
    else:
        return 2

def analyze_communication(comm):
    if comm < 30:
        return 2
    elif comm <= 59:
        return 1
    else:
        return 0

def analyze_battery(bat):
    if bat < 20:
        return 2
    elif bat <= 49:
        return 1
    else:
        return 0

def analyze_oxygen(ox):
    if ox < 80:
        return 2
    elif ox <= 89:
        return 1
    else:
        return 0

def analyze_stability(st):
    if st < 40:
        return 2
    elif st <= 69:
        return 1
    else:
        return 0

def classify_mission_cycle(risk_pt):
    sum_pts = sum(risk_pt)
    all_msg = [
        "Verificar controle térmico da missão.",
        "Tentar restabelecer contato com a base.",
        "Ativar modo de economia de energia.",
        "Acionar protocolo de suporte à vida.",
        "Reduzir operações não essenciais.",
        "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação.",
        "Monitorar sistemas em atenção e preparar plano de contingência.",
        "Manter operação normal e continuar monitoramento."
    ]
    rec_msg_idx = -1
    crit_idx = [i for i, x in enumerate(risk_pt) if x == 2]
    if len(crit_idx) > 1:
        rec_msg_idx = -3
    elif len(crit_idx) == 1:
        rec_msg_idx = crit_idx[0]
    elif not crit_idx:
        att_idx = [i for i, x in enumerate(risk_pt) if x == 1]
        if len(att_idx) > 1:
            rec_msg_idx = -2
        elif len(att_idx) == 1:
            rec_msg_idx = att_idx[0]

    if sum_pts <= 2:
        return "ESTÁVEL", all_msg[rec_msg_idx]
    elif sum_pts <= 5:
        return "EM ATENÇÃO", all_msg[rec_msg_idx]
    else:
        return "CRÍTICA", all_msg[rec_msg_idx]

def analyze_tendency():
    if risk_points[0] == risk_points[-1]:
        return "A missão permaneceu estável em relação ao início."
    elif risk_points[0] > risk_points[-1]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão apresentou tendência de piora."

def cycle_report(cycle_n):
    cycle_row = dados_missao[cycle_n]
    states = []
    states.append(analyze_temperature(cycle_row[TEMPERATURE_COL]))
    states.append(analyze_communication(cycle_row[COMMUNICATION_COL]))
    states.append(analyze_battery(cycle_row[BATTERY_COL]))
    states.append(analyze_oxygen(cycle_row[OXYGEN_COL]))
    states.append(analyze_stability(cycle_row[STABILITY_COL]))
    risk_points.append(states)
    mission_class, rec = classify_mission_cycle(risk_points[cycle_n])

    print(f"""CICLO {cycle_n + 1}
------------------------------------------------------------
Temperatura: {cycle_row[TEMPERATURE_COL]} °C | {alert_state[states[TEMPERATURE_COL]]} | {alert_msg[TEMPERATURE_COL][states[TEMPERATURE_COL]] if states[TEMPERATURE_COL] != 1 else (alert_msg[TEMPERATURE_COL][states[TEMPERATURE_COL]] if cycle_row[TEMPERATURE_COL] > 30 else alert_msg[TEMPERATURE_COL][-1])}
Comunicação: {cycle_row[COMMUNICATION_COL]}% | {alert_state[states[COMMUNICATION_COL]]} | {alert_msg[COMMUNICATION_COL][states[COMMUNICATION_COL]]}
Bateria: {cycle_row[BATTERY_COL]}% | {alert_state[states[BATTERY_COL]]} | {alert_msg[BATTERY_COL][states[BATTERY_COL]]}
Oxigênio: {cycle_row[OXYGEN_COL]}% | {alert_state[states[OXYGEN_COL]]} | {alert_msg[OXYGEN_COL][states[OXYGEN_COL]]}
Estabilidade: {cycle_row[STABILITY_COL]}% | {alert_state[states[STABILITY_COL]]} | {alert_msg[STABILITY_COL][states[STABILITY_COL]]}
Pontuação de risco do ciclo: {sum(risk_points[cycle_n])}
Classificação do ciclo: MISSÃO {mission_class}
Recomendação: {rec}
""")

def final_report():
    total_col_pts = [] # para descobrir que area teve mais pontos
    for i in range(len(risk_points[0])):
        total_col_pts.append(sum(row[i] for row in risk_points))
    total_row_pts = [] # para descobrir que ciclo teve mais pontos
    for i in range(len(risk_points)):
        total_row_pts.append(sum(col for col in risk_points[i]))

    print(f"""============================================================
RELATÓRIO FINAL DA MISSÃO
============================================================
Missão: {MISSION_NAME}
Equipe: {TEAM_NAME}

Quantidade de ciclos analisados: {len(dados_missao)}

Média de temperatura: {sum(row[TEMPERATURE_COL] for row in dados_missao) / len(dados_missao):.2f} °C
Média de comunicação: {sum(row[COMMUNICATION_COL] for row in dados_missao) / len(dados_missao):.2f}%
Média de bateria: {sum(row[BATTERY_COL] for row in dados_missao) / len(dados_missao):.2f}%
Média de oxigênio: {sum(row[OXYGEN_COL] for row in dados_missao) / len(dados_missao):.2f}%
Média de estabilidade: {sum(row[STABILITY_COL] for row in dados_missao) / len(dados_missao):.2f}%

Ciclo mais crítico: Ciclo {total_row_pts.index(max(total_row_pts)) + 1}
Maior pontuação de risco: {max(total_row_pts)}
Risco médio da missão: {sum(total_row_pts)/len(total_row_pts):.2f}
Quantidade de ciclos críticos: {len([i for i in total_row_pts if i > 5])}

Tendência da missão:
{analyze_tendency()}

Pontuação acumulada por área:
Temperatura interna: {total_col_pts[TEMPERATURE_COL]} pontos
Comunicação com a base: {total_col_pts[COMMUNICATION_COL]} pontos
Sistema de energia: {total_col_pts[BATTERY_COL]} pontos
Suporte de oxigênio: {total_col_pts[OXYGEN_COL]} pontos
Estabilidade operacional: {total_col_pts[STABILITY_COL]} pontos

Área mais afetada:
{areas_monitoradas[total_col_pts.index(max(total_col_pts))]}

Classificação final da missão:
MISSÃO EM ATENÇÃO

Conclusão:
A missão apresentou instabilidade relevante durante a operação. Apesar
da tentativa de recuperação no último ciclo, ainda existem sistemas em
atenção e a equipe deve manter o plano de contingência ativo.
""")

def mission_report():
    print(f"""============================================================
MISSION CONTROL AI
============================================================
Missão: {MISSION_NAME}
Equipe: {TEAM_NAME}
Quantidade de ciclos analisados: {len(dados_missao)}
============================================================
""")
    for cycle_n in range(0, len(dados_missao)):
        cycle_report(cycle_n)
    final_report()

mission_report()