import streamlit as st

st.set_page_config(page_title="Paradoxo de Simpson", layout="centered")

st.title("Quem disse que conta não vira aplicativo?")
st.subheader("Visualizando o Paradoxo de Simpson")

st.markdown("""
Vamos analisar **duas situações simples** usando apenas contas básicas.
Depois, vamos juntar tudo e ver o que acontece.
""")

st.divider()

# Dados (inventados e pequenos)
A1_sucesso, A1_total = 9, 10
B1_sucesso, B1_total = 8, 10

A2_sucesso, A2_total = 1, 10
B2_sucesso, B2_total = 2, 10

# Botão 1 — Situação 1
if st.button("🔹 Situação 1"):
    taxa_A1 = A1_sucesso / A1_total
    taxa_B1 = B1_sucesso / B1_total

    st.write(f"Grupo A: {A1_sucesso}/{A1_total} = {taxa_A1:.0%}")
    st.write(f"Grupo B: {B1_sucesso}/{B1_total} = {taxa_B1:.0%}")

    st.success("➡️ Conclusão: Grupo A é melhor nesta situação.")

# Botão 2 — Situação 2
if st.button("🔹 Situação 2"):
    taxa_A2 = A2_sucesso / A2_total
    taxa_B2 = B2_sucesso / B2_total

    st.write(f"Grupo A: {A2_sucesso}/{A2_total} = {taxa_A2:.0%}")
    st.write(f"Grupo B: {B2_sucesso}/{B2_total} = {taxa_B2:.0%}")

    st.success("➡️ Conclusão: Grupo B é melhor nesta situação.")

# Botão 3 — Agregado (o paradoxo)
if st.button("🔍 Ver resultado total"):
    total_A = (A1_sucesso + A2_sucesso) / (A1_total + A2_total)
    total_B = (B1_sucesso + B2_sucesso) / (B1_total + B2_total)

    st.write(f"Grupo A total: {(A1_sucesso + A2_sucesso)}/{(A1_total + A2_total)} = {total_A:.0%}")
    st.write(f"Grupo B total: {(B1_sucesso + B2_sucesso)}/{(B1_total + B2_total)} = {total_B:.0%}")

    st.error("⚠️ Conclusão: O resultado geral contradiz as análises separadas!")

    st.markdown("""
### 🤯 O que aconteceu?
Cada conta está **correta**.  
O erro não está na matemática, mas **na forma de agrupar os dados**.

Isso é o **Paradoxo de Simpson**.
""")
