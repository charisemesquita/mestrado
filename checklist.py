import streamlit as st

st.set_page_config(page_title="Checklist de Acessibilidade em Laboratórios", layout="wide")

st.title("🔬 Avaliação de Acessibilidade Fisico-Funcional em Laboratórios")
st.markdown("**Instrumento de Diagnóstico Rápido para Ambientes de Ensino**")

# Estrutura do Checklist com os 6 Blocos e 40 Itens
checklist_data = {
    "BLOCO 1 — ACESSO E CIRCULAÇÃO NO ESPAÇO": [
        "1.1 A rota de acesso ao laboratório a partir da entrada do edifício é livre de obstáculos?",
        "1.2 Existe rota acessível (rampa ou elevador) para o laboratório em pavimento diferente do térreo?",
        "1.3 A largura do corredor de acesso ao laboratório é igual ou superior a 120 cm?",
        "1.4 A porta de entrada do laboratório tem largura livre mínima de 80 cm?",
        "1.5 A porta possui maçaneta de alavanca ou outro acionamento acessível?",
        "1.6 O piso do acesso e interior do laboratório é antiderrapante e sem irregularidades?",
        "1.7 A largura entre bancadas permite circulação de cadeira de rodas (mínimo 90 cm)?",
        "1.8 Existe pelo menos uma área de manobra de 150 cm de diâmetro dentro do laboratório?",
        "1.9 Os corredores internos estão livres de equipamentos ou objetos que obstruam a passagem?",
        "1.10 Há sinalização visual no piso identificando rotas de circulação e saídas de emergência?"
    ],
    "BLOCO 2 — SUPERFÍCIES DE TRABALHO E MOBILIÁRIO": [
        "2.1 Existe ao menos uma bancada com altura regulável ou adaptada (altura livre inferior ≥ 73 cm)?",
        "2.2 O espaço sob a bancada é suficiente para aproximação frontal (profundidade mínima 50 cm)?",
        "2.3 As bancadas têm borda frontal livre de obstáculos fixos que impeçam a aproximação?",
        "2.4 Os controles, torneiras e registros estão em altura de alcance acessível (máximo 120 cm)?",
        "2.5 Os controles e torneiras podem ser operados com uma única mão ou sem preensão fina?",
        "2.6 Há cadeiras ou bancos ajustáveis em altura disponíveis no laboratório?",
        "2.7 Existe espaço reservado para estacionamento de cadeira de rodas sem obstrução?"
    ],
    "BLOCO 3 — EQUIPAMENTOS E DISPOSITIVOS": [
        "3.1 Os equipamentos de uso frequente estão posicionados em superfícies de altura acessível?",
        "3.2 Há adaptações disponíveis para uso de microscópios por pessoas com deficiência?",
        "3.3 Displays e painéis possuem contraste visual adequado ou alternativas táteis/sonoras?",
        "3.4 Existem adaptações para manuseio de materiais por limitação de destreza manual?",
        "3.5 Os equipamentos digitais/computadores são compatíveis com tecnologias assistivas?",
        "3.6 As conexões de gás, água e energia são flexíveis para reposicionamento?",
        "3.7 As capelas de exaustão possuem altura regulável ou versão acessível?",
        "3.8 As pias possuem altura acessível (73 cm livre abaixo) e torneira sem preensão fina?"
    ],
    "BLOCO 4 — SEGURANÇA E EMERGÊNCIA": [
        "4.1 Extintores, chuveiros e lava-olhos em local acessível e altura de até 100 cm?",
        "4.2 O sistema de alarme de emergência inclui sinalização sonora E visual?",
        "4.3 Os EPIs disponíveis estão disponíveis em diferentes tamanhos e/ou adaptações?",
        "4.4 Existe protocolo documentado de evacuação que contemple pessoas com deficiência?",
        "4.5 A iluminação do laboratório é uniforme e sem reflexos, adequada para baixa visão?"
    ],
    "BLOCO 5 — COMUNICAÇÃO E SINALIZAÇÃO": [
        "5.1 O laboratório possui identificação externa em texto e Braille/relevo?",
        "5.2 A sinalização interna de segurança está em alto contraste?",
        "5.3 Roteiros e protocolos experimentais estão em formatos alternativos acessíveis?",
        "5.4 Rótulos de reagentes estão em fonte legível (mínimo 12pt) e fácil visualização?",
        "5.5 Existe material de orientação sobre normas de segurança em formato acessível?",
        "5.6 Informações do quadro são verbalizadas ou disponibilizadas em material concomitante?"
    ],
    "BLOCO 6 — TECNOLOGIA ASSISTIVA": [
        "6.1 O laboratório dispõe de recursos de TA (lupas, leitores de tela, softwares)?",
        "6.2 Existe inventário ou registro institucional dos recursos de TA disponíveis?",
        "6.3 Os softwares utilizados nas práticas são compatíveis com tecnologias assistivas?",
        "6.4 Há responsável técnico ou docente capacitado para orientar o uso de TA?"
    ]
}

# Formulário de Avaliação
laboratorio_nome = st.sidebar.text_input("Nome do Laboratório Avaliado:", "Laboratório Multi 01")
avaliador_nome = st.sidebar.text_input("Nome do Avaliador:", "Pesquisador")

respostas_globais = {}
conformidade_blocos = {}

st.subheader(f"Avaliação: {laboratorio_nome}")

for bloco, perguntas in checklist_data.items():
    with st.expander(bloco, expanded=True):
        respostas_bloco = []
        for q in perguntas:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(q)
            with col2:
                resp = st.selectbox("", ["Sim", "Não", "Não se Aplica"], key=q, label_visibility="collapsed")
                respostas_bloco.append(resp)
        
        # Cálculo de Conformidade do Bloco
        sims = respostas_bloco.count("Sim")
        naos = respostas_bloco.count("Não")
        validos = sims + naos
        
        porcentagem = (sims / validos * 100) if validos > 0 else 0.0
        conformidade_blocos[bloco] = porcentagem
        st.metric(label=f"Conformidade — {bloco.split('—')[1].strip()}", value=f"{porcentagem:.1f}%")

st.markdown("---")

# Painel Geral de Resultados
st.header("📊 Resultado Final da Auditoria")
cols = st.columns(len(conformidade_blocos))
idx = 0
for bloco, perc in conformidade_blocos.items():
    cols[idx].metric(f"Bloco {idx+1}", f"{perc:.1f}%")
    idx += 1

# Média Geral do Laboratório
total_sims = sum([respostas_bloco.count("Sim") for respostas_bloco in respostas_globais.values()])
total_naos = sum([respostas_bloco.count("Não") for respostas_bloco in respostas_globais.values()])

st.button("💾 Exportar Relatório de Auditoria")
