import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Sócio 5 Estrelas", page_icon="🦊", layout="wide")

if "efeito" not in st.session_state:
    st.session_state.efeito = None

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #00122e 0%, #005BA3 50%, #4facfe 100%);
    background-attachment: fixed;
}
.stButton>button {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border: 1px solid white;
    border-radius: 15px;
}
h1, h2, h3, p, span, label { color: white !important; }

.fall, .joker {
    position: fixed;
    top: -50px;
    font-size: 30px;
    animation: fall linear infinite;
    z-index: 9999;
}
@keyframes fall {
    0% { transform: translateY(-50px); opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

def carregar_imagem(nome_base):
    for ext in [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]:
        caminho = f"{nome_base}{ext}"
        if os.path.exists(caminho):
            return caminho
    return None

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bc/Cruzeiro_Esporte_Clube_logo.svg", width=80)
    st.title("Painel do Sócio")

st.markdown("<h1 style='text-align:center;'>Sócio 5 estrelas by Carol Bastos</h1>", unsafe_allow_html=True)

st.markdown("### 🎵 Solta o Hino, Torcedor!")
st.video("https://www.youtube.com/watch?v=aeJzEJ8pcXg")

st.divider()

st.header("🏆 Planos 5 estrelas")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Estrelas do Povo")
    img = carregar_imagem("gerson")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 21,00/mês")
    if st.button("Assinar Estrelas do Povo", key="povo", use_container_width=True):
        st.session_state.efeito = "joker"

with col2:
    st.subheader("Cruzeiro Sempre")
    img = carregar_imagem("mp10")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 62,00/mês")
    if st.button("Assinar Cruzeiro Sempre", key="sempre", use_container_width=True):
        st.snow()

with col3:
    st.subheader("K-abuloso Max")
    img = carregar_imagem("kaio")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 150,00/mês")
    if st.button("Assinar K-abuloso Max", key="max", use_container_width=True):
        st.session_state.efeito = "gol"

st.divider()

col_esq, col_dir = st.columns([2,1])

with col_esq:
    st.header("📊 Crescimento de Sócios")
    dados = pd.DataFrame({'Mês':['Jan','Fev','Mar','Abr','Mai','Jun'],'Novos Sócios':[4500,5200,6100,5800,7500,9000]})
    st.bar_chart(dados.set_index('Mês'))

    st.header("📖 Nossa História")
    with st.expander("⭐ História do Clube"):
        st.write("""
A história do Cruzeiro Esporte Clube começa em 2 de janeiro de 1921...
(continua sua história completa aqui igual antes)
""")

img = carregar_imagem("raposao")
if img: st.image(img, width=500)

with st.expander("⭐ 2003 - Tríplice Coroa"):
    st.write("""
A Tríplice Coroa do Cruzeiro refere-se ao feito histórico de 2003...
""")

img = carregar_imagem("fototrofeu")
if img: st.image(img, width=500)

st.header("📍 Nossa Casa")
st.map(pd.DataFrame({'lat':[-19.8659],'lon':[-43.9711]}))

with col_dir:
    st.header("🏟️ Check-in")
    with st.form("check"):
        setor = st.selectbox("Setor do Estádio", ["Amarelo","Laranja","Vermelho","Roxo"])
        if st.form_submit_button("Confirmar Presença"):
            st.toast("Check-in feito!")

    st.header("💬 Mural Azul")
    with st.form("mural"):
        nome = st.text_input("Seu Nome")
        msg = st.text_area("Mensagem")
        if st.form_submit_button("Postar"):
            st.success("Mensagem postada!")

# EFEITOS VISUAIS CONTROLADOS
if st.session_state.efeito == "joker":
    st.toast("🃏 Modo Coringa ativado!")
    st.markdown("""
    <div class="joker" style="left:10%; animation-duration:3s;">🃏</div>
    <div class="joker" style="left:20%; animation-duration:4s;">🃏</div>
    <div class="joker" style="left:30%; animation-duration:5s;">🃏</div>
    <div class="joker" style="left:40%; animation-duration:3.5s;">🃏</div>
    """, unsafe_allow_html=True)

elif st.session_state.efeito == "gol":
    st.toast("⚽ GOOOOOL DO CABULOSO!")
    st.markdown("""
    <div class="fall" style="left:5%; animation-duration:3s;">⚽</div>
    <div class="fall" style="left:15%; animation-duration:4s;">GOL</div>
    <div class="fall" style="left:25%; animation-duration:5s;">⚽</div>
    <div class="fall" style="left:35%; animation-duration:3.5s;">GOL</div>
    <div class="fall" style="left:45%; animation-duration:4.5s;">⚽</div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.write("© 2026 - Desenvolvido com 💙 por Carol Bastos")





