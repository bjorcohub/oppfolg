import streamlit as st

st.set_page_config(page_title="KPI Oppfølging", layout="centered")
st.title("KPI Oppfølging")

# Initialize session state for KPI blocks
if "kpi_blocks" not in st.session_state:
    st.session_state.kpi_blocks = [{"id": 0}]

def add_block():
    st.session_state.kpi_blocks.append({"id": len(st.session_state.kpi_blocks)})

def remove_block(index):
    st.session_state.kpi_blocks.pop(index)
    st.experimental_rerun()

st.subheader("KPI-skjema")

# Display KPI entry blocks
for i, block in enumerate(st.session_state.kpi_blocks):
    with st.expander(f"KPI {i + 1}", expanded=True):
        kpi = st.text_input("KPI", key=f"kpi_{i}")
        tiltak_sist = st.text_area("Tiltak sist", height=100, key=f"tiltak_sist_{i}")
        status_sist = st.text_area("Status sist", height=100, key=f"status_sist_{i}")
        status_no = st.text_area("Status no", height=100, key=f"status_no_{i}")
        fungerte = st.text_area("Kva fungerte / fungerte ikkje", height=150, key=f"fungerte_{i}")
        mal_neste = st.text_area("Mål til neste gang", height=100, key=f"mal_neste_{i}")
        tiltak_neste = st.text_area("Tiltak til neste gang", height=100, key=f"tiltak_neste_{i}")

        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("🗑️ Fjern", key=f"remove_{i}"):
                remove_block(i)

st.button("➕ Legg til ny KPI", on_click=add_block)

# Show full + short summary
if st.button("📋 Vis oppsummering"):
    st.subheader("🧾 Full oppsummering")
    for i, block in enumerate(st.session_state.kpi_blocks):
        kpi = st.session_state.get(f"kpi_{i}", "")
        tiltak_sist = st.session_state.get(f"tiltak_sist_{i}", "")
        status_sist = st.session_state.get(f"status_sist_{i}", "")
        status_no = st.session_state.get(f"status_no_{i}", "")
        fungerte = st.session_state.get(f"fungerte_{i}", "")
        mal_neste = st.session_state.get(f"mal_neste_{i}", "")
        tiltak_neste = st.session_state.get(f"tiltak_neste_{i}", "")

        st.markdown(f"""
        **KPI {i+1}: {kpi}**
        - **Tiltak sist:** {tiltak_sist}
        - **Status sist:** {status_sist}
        - **Status no:** {status_no}
        - **Kva fungerte / fungerte ikkje:** {fungerte}
        - **Mål til neste gang:** {mal_neste}
        - **Tiltak til neste gang:** {tiltak_neste}
        """)

    st.markdown("---")
    st.subheader("📌 Kort oppsummering")
    for i, block in enumerate(st.session_state.kpi_blocks):
        kpi = st.session_state.get(f"kpi_{i}", "")
        mal_neste = st.session_state.get(f"mal_neste_{i}", "")
        tiltak_neste = st.session_state.get(f"tiltak_neste_{i}", "")
        st.markdown(f"""
        **{i+1}. {kpi}**
        - 🎯 *Mål:* {mal_neste}
        - 🛠️ *Tiltak:* {tiltak_neste}
        """)
