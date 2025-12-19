import streamlit as st

st.title("Meu app online")

st.write("Se você está vendo isso, Python está rodando na web 🙂")

numero = st.slider("Escolha um número", 0, 100, 10)

st.write("O quadrado do número é:", numero**2)

