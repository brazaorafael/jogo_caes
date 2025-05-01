
import streamlit as st
from collections import Counter

# Configurações da página
st.set_page_config(page_title="Qual dos meus cães é você?", layout="centered")

st.title("🐶 Qual dos meus cães é você?")
st.write("Responda às perguntas abaixo e descubra com qual dos meus cães você mais se parece!")

# Perguntas e alternativas
perguntas = {
    "1. Qual dessas situações mais combina com você?": {
        "Ficar quieto no seu canto sem ser incomodado": ["Sochi", "Panda", "Manju"],
        "Procurar um lugar ao sol e aproveitar o momento": ["Boo", "Pancake", "Dalai"],
        "Correr por aí e fazer bagunça": ["Harley", "Bindi", "Mochi"],
        "Observar tudo ao redor, bem de boa": ["Dalai", "Orquídea", "Sochi"],
        "Ficar colado em alguém pedindo carinho": ["Agnes", "Boo", "Sunshine"]
    },
    "2. Quando está com preguiça, o que você faz?": {
        "Dorme de qualquer jeito, até comendo": ["Panda", "Sunshine"],
        "Procura um lugar quentinho e confortável": ["Manju", "Pancake"],
        "Mesmo cansado, corre atrás de um brinquedo": ["Mit Mit", "Mochi"],
        "Deita no colo de alguém": ["Boo", "Pancake", "Agnes"],
        "Dá uma cochilada mas fica de olho em tudo": ["Sochi", "Dalai"]
    },
    "3. O que você mais gosta de fazer em um dia normal?": {
        "Fazer bagunça com os outros": ["Harley", "Bindi", "Mochi"],
        "Observar o mundo em silêncio": ["Dalai", "Panda"],
        "Procurar comida gostosa": ["Harley", "Boo", "Sochi"],
        "Brincar com bola ou brinquedos": ["Mit Mit", "Bindi"],
        "Ficar no seu canto, mas com um pouco de carinho": ["Agnes", "Manju", "Orquídea"]
    },
    "4. Como você reage a gente nova?": {
        "Recebe todo mundo com alegria": ["Boo", "Mochi", "Bindi"],
        "Gosta, mas só se vier com carinho": ["Agnes", "Sunshine", "Pancake"],
        "Fica desconfiado": ["Orquídea", "Panda", "Sochi"],
        "Ignora e segue sua vida": ["Dalai", "Manju"],
        "Corre pra brincar": ["Mit Mit", "Harley"]
    },
    "5. Qual dessas frases mais combina com você?": {
        "Sou tranquilo, mas adoro brincar quando estou no clima": ["Dalai", "Sochi", "Pancake"],
        "Sou um furacão com quatro patas": ["Harley", "Bindi", "Mochi"],
        "Meu lugar é no colo de alguém": ["Boo", "Agnes", "Sunshine"],
        "Sou tímido, mas carinhoso com quem eu gosto": ["Orquídea", "Manju", "Panda"],
        "Só me chama se tiver brinquedo ou comida": ["Mit Mit", "Harley", "Boo"]
    }
}

# Guardar respostas
respostas = []

# Mostrar perguntas em sequência
with st.form("quiz_form"):
    for pergunta, alternativas in perguntas.items():
        resposta = st.radio(pergunta, list(alternativas.keys()), key=pergunta)
        respostas.append(resposta)
    submitted = st.form_submit_button("Descobrir!")

# Lógica do resultado
if submitted:
    pontos = []
    for i, resposta in enumerate(respostas):
        valores = list(perguntas.values())[i][resposta]
        pontos.extend(valores)

    if pontos:
        mais_pontuado = Counter(pontos).most_common(1)[0][0]
        st.subheader(f"Você é como... {mais_pontuado}!")

        # Descrições
        descricoes = {
            "Sochi": "Independente, intensa e com personalidade forte. Quando quer brincar, ninguém segura!",
            "Boo": "Carente, amoroso e sempre atrás de uma guloseima. Seu lugar é no colo!",
            "Agnes": "Meiguice pura. Carinhosa, delicada e cheia de afeto.",
            "Harley": "Pura energia! Louca por aventura, comida e diversão sem fim.",
            "Sunshine": "Preguiçosa e desajeitada, mas com o coração mais doce do mundo!",
            "Panda": "Discreta e tranquila. Ama a preguiça e faz tudo no seu ritmo.",
            "Mit Mit": "Brincalhão, curioso e com energia de sobra! Menininho da casa.",
            "Dalai": "O sábio da turma. Gosta de brincar, mas também de contemplar a natureza.",
            "Bindi": "Pequena e elétrica! Corre, beija e espalha alegria.",
            "Orquídea": "Sensível e reservada. Só se abre com quem conquista seu coração.",
            "Mochi": "Engraçada, barulhenta e cheia de personalidade. Ama um show!",
            "Manju": "Calminha e amorosa, mas gosta de um cantinho quentinho e tranquilo.",
            "Pancake": "Zen total. Adora carinho na barriga, colo e sossego."
        }

        st.write(descricoes[mais_pontuado])

        # Mostrar imagem se houver
        from pathlib import Path
        img_path = Path(f"cards/{mais_pontuado.lower()}.png")
        if img_path.exists():
            st.image(str(img_path), use_column_width=True)
        else:
            st.info("Imagem do card ainda não foi adicionada.")
