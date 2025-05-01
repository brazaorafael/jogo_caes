import streamlit as st
from collections import Counter
from pathlib import Path

# Configurações da página
st.set_page_config(page_title="Quiz dos Cães - Carrossel", layout="centered")

# Perguntas e alternativas
perguntas = [
    ("1. Qual dessas situações mais combina com você?", {
        "Ficar quieto no seu canto sem ser incomodado": ["Sochi", "Panda", "Manju"],
        "Procurar um lugar ao sol e aproveitar o momento": ["Boo", "Pancake", "Dalai"],
        "Correr por aí e fazer bagunça": ["Harley", "Bindi", "Mochi"],
        "Observar tudo ao redor, bem de boa": ["Dalai", "Orquídea", "Sochi"],
        "Ficar colado em alguém pedindo carinho": ["Agnes", "Boo", "Sunshine"]
    }),
    # ... (outras perguntas seguem o mesmo formato)
]

# Inicializa estado
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(perguntas)

def next_q():
    if st.session_state.answers[st.session_state.idx] is not None:
        st.session_state.idx += 1

# Barra de progresso
st.progress((st.session_state.idx + 1) / len(perguntas))

# Exibe pergunta atual
pergunta, opts = perguntas[st.session_state.idx]
st.markdown(f"### {pergunta}")
choice = st.radio("", list(opts.keys()),
                  index=0 if st.session_state.answers[st.session_state.idx] is None 
                          else list(opts.keys()).index(st.session_state.answers[st.session_state.idx]))
st.session_state.answers[st.session_state.idx] = choice

# Navegação: apenas Próxima ou Ver Resultado
if st.session_state.idx < len(perguntas) - 1:
    st.button("Próxima ➡️", on_click=next_q)
else:
    if st.button("Ver Resultado"):
        pontos = []
        for i, resp in enumerate(st.session_state.answers):
            pontos.extend(perguntas[i][1][resp])
        mais = Counter(pontos).most_common(1)[0][0]

        descr = {
            "Sochi":"Independente, intensa e com personalidade forte.",
            "Boo":"Carente, amoroso e sempre atrás de uma guloseima.",
            "Agnes":"Carinhosa e meiga, impossível resistir!",
            "Harley":"Cheia de energia e pronta pra aventura.",
            "Sunshine":"Preguiçosa, desajeitada e amorosa.",
            "Panda":"Tranquila e amável, no seu ritmo.",
            "Mit Mit":"Curioso e brincalhão, energia pura.",
            "Dalai":"Sábio e contemplativo, zen.",
            "Bindi":"Pequenina e elétrica, pura alegria.",
            "Orquídea":"Reservada, mas de coração sensível.",
            "Mochi":"Engraçada e barulhenta, ama diversão.",
            "Manju":"Quietinha e carinhosa, adora aconchego.",
            "Pancake":"Zen e calma, ama um colo."
        }

        st.success(f"**Você é como... {mais}!**")
        st.write(descr[mais])

        img_path = Path(f"cards/{mais}.png")
        if img_path.exists():
            st.image(str(img_path), use_container_width=True)
        else:
            st.error(f"Imagem não encontrada: {img_path.name}")
