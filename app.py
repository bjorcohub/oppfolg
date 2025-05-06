import streamlit as st

st.title("KPI Oppfølging")

# KPI
kpi = st.text_input("KPI")

# Status sist
status_sist = st.text_area("Status sist", height=100)

# Tiltak
tiltak = st.text_area("Tiltak", height=100)

# Status no
status_no = st.text_area("Status no", height=100)

# Kva fungerte / fungerte ikkje
fungerte = st.text_area("Kva fungerte / fungerte ikkje", height=150)

# Mål til neste gang
mal_neste = st.text_area("Mål til neste gang", height=100)

# Tiltak til neste gang
tiltak_neste = st.text_area("Tiltak til neste gang", height=100)

# Optional: Show collected data
if st.button("Vis sammendrag"):
    st.subheader("Sammendrag")
    st.write(f"**KPI:** {kpi}")
    st.write(f"**Status sist:** {status_sist}")
    st.write(f"**Tiltak:** {tiltak}")
    st.write(f"**Status no:** {status_no}")
    st.write(f"**Kva fungerte / fungerte ikkje:** {fungerte}")
    st.write(f"**Mål til neste gang:** {mal_neste}")
    st.write(f"**Tiltak til neste gang:** {tiltak_neste}")
