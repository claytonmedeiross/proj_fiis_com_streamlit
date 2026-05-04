import streamlit as st
import yfinance as yf

# 🔹 IMAGEM + PERFIL (TOPO)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("foto.png", width=150)
    st.markdown("### Clayton Medeiros")
    st.markdown("Analista de Dados | FIIs 📊")

st.title("📊 Dashboard de FIIs")

lista_fiis = [
    "MXRF11.SA",  # Maxi Renda
    "HGLG11.SA",  # Logística
    "KNRI11.SA",  # Híbrido
    "XPML11.SA",  # Shoppings
    "RBHY11.SA",  # High Yield
    
    "KNCR11.SA",  # Papel (CRI)
    "KNIP11.SA",  # Papel (IPCA)
    "CPTS11.SA",  # Papel
    "BTLG11.SA",  # Logística
    "TRXF11.SA",  # Renda Urbana
    
    "CPLG11.SA",  # Logística (muito negociado)
    "CPUR11.SA",  # Renda urbana
    "GSFI11.SA",  # Híbrido
    
    "VISC11.SA",  # Shoppings
    "HSML11.SA",  # Shoppings
    "MALL11.SA",  # Shoppings
    
    "LVBI11.SA",  # Logística
    "XPLG11.SA",  # Logística
    "BRCO11.SA",  # Logística
    
    "HGRE11.SA",  # Lajes corporativas
    "PVBI11.SA",  # Lajes premium
    
    "RBRY11.SA",  # Papel high yield
    "MCCI11.SA",  # Papel
    "KNSC11.SA"   # Papel
]
ticker = st.selectbox("Escolha um FII:", lista_fiis)

nome_ticker = ticker.replace(".SA", "")
st.subheader(f"📈 {nome_ticker}")

@st.cache_data
def carregar_dados(ticker):
    ativo = yf.Ticker(ticker)
    try:
        info = ativo.info
    except:
        info = {}
    dados = ativo.history(period="6mo")
    return dados, info

with st.spinner("Carregando dados..."):
    dados, info = carregar_dados(ticker)

st.subheader("📌 Informações do ativo")

nome_ativo = info.get("shortName", "N/A")
preco_atual = info.get("regularMarketPrice")

st.write(f"**Nome:** {nome_ativo}")

if preco_atual:
    st.metric("Preço atual", f"R$ {preco_atual:.2f}")
else:
    st.write("**Preço atual:** N/A")

st.subheader("📈 Preço de Fechamento")

if dados.empty:
    st.error("Sem dados para esse ativo 😕")
else:
    st.line_chart(dados["Close"])

st.subheader("📅 Dados recentes")
st.write(dados.tail())

st.subheader("📊 Volume negociado")
st.bar_chart(dados["Volume"])