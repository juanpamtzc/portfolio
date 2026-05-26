import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="centered")

st.title("Computational Mathematics Portfolio")
st.write("Welcome. I build scalable, mathematically rigorous computational models.")

st.divider()

# Project 1 Entry
st.subheader("🔵 Blue vs. Red: Game-Theoretic Optimizer")
st.write("A vectorized expected utility model computing survival strategies under existential risk.")
st.link_button("Launch Simulator", "https://red-vs-blue.streamlit.app/#2-parameter-space-sweep")
st.link_button("View Source Code", "https://github.com/juanpamtzc/red_vs_blue")

# Project 2 Entry (For later)
# st.subheader("Next Project...")