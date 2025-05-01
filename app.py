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
    ("2. Quando está com preguiça, o que você faz?", {
        "Dorme de qualquer jeito, até comendo": ["Panda", "Sunshine"],
        "Procura um lugar quentinho e confortável": ["Manju", "Pancake"],
        "Mesmo cansado, corre atrás de um brinquedo": ["Mit Mit", "Mochi"],
        "Deita no colo de alguém": ["Boo", "Pancake", "Agnes"],
        "Dá uma cochilada mas fica de olho em tudo": ["Sochi", "Dalai"]
    }),
    ("3. O que você mais gosta de fazer em um dia normal?", {
        "Fazer bagunça com os outros": ["Harley", "Bindi", "Mochi"],
        "Observar o mundo em silêncio": ["Dalai", "Panda"],
        "Procurar comida gostosa": ["Harley", "Boo", "Sochi"],
        "Brincar com bola ou brinquedos": ["Mit Mit", "Bindi"],
        "Ficar no seu canto, mas com um pouco de carinho": ["Agnes", "Manju", "Orquídea"]
    }),
    ("4. Como você reage a gente nova?", {
        "Recebe todo mundo com alegria": ["Boo", "Mochi", "Bindi"],
        "Gosta, mas só se vier com carinho": ["Agnes", "Sunshine", "Pancake"],
        "Fica desconfiado": ["Orquídea", "Panda", "Sochi"],
        "Ignora e segue sua vida": ["Dalai", "Manju"],
        "Corre pra brincar": ["Mit Mit", "Harley"]
    }),
    ("5. Qual dessas frases mais combina com você?", {
        "Sou tranquilo, mas adoro brincar quando estou no clima": ["Dalai", "Sochi", "Pancake"],
        "Sou um furacão com quatro patas": ["Harley", "Bindi", "Mochi"],
        "Meu lugar é no colo de alguém": ["Boo", "Agnes", "Sunshine"],
        "Sou tímido, mas carinhoso com quem eu gosto": ["Orquídea", "Manju", "Panda"],
        "Só me chama se tiver brinquedo ou comida": ["Mit Mit", "Harley", "Boo"]
    }),
]

# Inicializa estado
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(perguntas)

def next_q():
    if st.session_state.answers[st.session_state.idx] is not None:
        st.session_state.idx += 1

def prev_q():
    if st.session_state.idx > 0:
        st.session_state.idx -= 1

# Barra de progresso
st.progress((st.session_state.idx + 1) / len(perguntas))

# Exibe pergunta atual
pergunta, opts = perguntas[st.session_state.idx]
st.markdown(f"### {pergunta}")
choice = st.radio("", list(opts.keys()), index=0 if st.session_state.answers[st.session_state.idx] is None else list(opts.keys()).index(st.session_state.answers[st.session_state.idx]))
st.session_state.answers[st.session_state.idx] = choice

# Navegação
col1, _, col3 = st.columns([1, 1, 1])
with col1:
    if st.session_state.idx > 0:
        st.button("⬅️ Anterior", on_click=prev_q)
with col3:
    if st.session_state.idx < len(perguntas) - 1:
        st.button("Próxima ➡️", on_click=next_q)

# Resultado no fim
if st.session_state.idx == len(perguntas) - 1 and st.session_state.answers[-1]:
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

        img_path = Path(f"cards/{mais}.png")  # usa nome com maiúscula
        if img_path.exists():
            st.image(str(img_path), use_column_width=True)
        else:
            st.error(f"Imagem não encontrada em cards/: {img_path.name}")
