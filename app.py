import streamlit as st
import pandas as pd
import os
from datetime import datetime, timezone

st.set_page_config(page_title="Sócio 5 Estrelas", page_icon="🦊", layout="wide")

BASE_DIR = os.path.dirname(__file__)

def carregar_imagem(nome):
    for ext in [".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"]:
        caminho = os.path.join(BASE_DIR, f"{nome}{ext}")
        if os.path.exists(caminho):
            return caminho
    return None


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

with st.sidebar:
    st.title("Painel do Sócio")
    st.subheader("🗓️ Próximo Jogo")

    data_jogo = datetime(2026, 2, 8, 16, 0, tzinfo=timezone.utc)
    agora = datetime.now(timezone.utc)
    dias_restantes = max(0, (data_jogo - agora).days)

    st.metric("Dias para o Clássico", dias_restantes)

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
    if st.button("Assinar Estrelas do Povo", use_container_width=True):
        st.toast("🃏 Modo Coringa ativado!")

with col2:
    st.subheader("Cruzeiro Sempre")
    img = carregar_imagem("mp10")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 62,00/mês")
    if st.button("Assinar Cruzeiro Sempre", use_container_width=True):
        st.snow()

with col3:
    st.subheader("K-abuloso Max")
    img = carregar_imagem("kaio")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 150,00/mês")
    if st.button("Assinar K-abuloso Max", use_container_width=True):
        st.toast("⚽ GOOOOOL DO CABULOSO!")

st.divider()

st.header("📊 Crescimento de Sócios")
dados = pd.DataFrame({
    'Mês':['Jan','Fev','Mar','Abr','Mai','Jun'],
    'Novos Sócios':[4500,5200,6100,5800,7500,9000]
})
st.bar_chart(dados.set_index('Mês'))

st.header("📖 Nossa História")
with st.expander("⭐ Fundação e Glórias"):
    st.write("O Cruzeiro foi fundado em 1921 e se tornou um dos maiores clubes do Brasil.")

img = carregar_imagem("raposao")
if img: st.image(img, width=500)

with st.expander("⭐ Tríplice Coroa 2003"):
    st.write("Em 2003 o Cruzeiro conquistou Mineiro, Copa do Brasil e Brasileirão.")

img = carregar_imagem("fototrofeu")
if img: st.image(img, width=500)

st.header("📍 Nossa Casa")
st.map(pd.DataFrame({'lat':[-19.8659],'lon':[-43.9711]}))

st.markdown("---")
st.write("© 2026 - Desenvolvido com 💙 por Carol Bastos")







