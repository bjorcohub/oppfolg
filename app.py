import streamlit as st
from datetime import date
import uuid

st.set_page_config(page_title="KPI Skjema", layout="centered")
st.title("📝 KPI Skjema")

# Initialize session state
if "kpi_blocks" not in st.session_state:
    st.session_state.kpi_blocks = [str(uuid.uuid4())]

# Name and date input
name = st.text_input("Navn")
dato = st.date_input("Dato", value=date.today())

def remove_block(block_id):
    st.session_state.kpi_blocks = [b for b in st.session_state.kpi_blocks if b != block_id]
    for suffix in ["kpi", "tiltak_sist", "status_sist", "status_no", "fungerte", "mal_neste", "tiltak_neste"]:
        st.session_state.pop(f"{suffix}_{block_id}", None)
    st.experimental_rerun()

# Render KPI blocks
for block_id in st.session_state.kpi_blocks:
    with st.container():
        st.markdown(f"### KPI")
        kpi = st.text_area("KPI", height=50, key=f"kpi_{block_id}")
        tiltak_sist = st.text_area("Tiltak sist", height=100, key=f"tiltak_sist_{block_id}")
        status_sist = st.text_area("Status sist", height=100, key=f"status_sist_{block_id}")
        status_no = st.text_area("Status no", height=100, key=f"status_no_{block_id}")
        fungerte = st.text_area("Kva fungerte / fungerte ikkje", height=150, key=f"fungerte_{block_id}")
        mal_neste = st.text_area("Mål til neste gang", height=100, key=f"mal_neste_{block_id}")
        tiltak_neste = st.text_area("Tiltak til neste gang", height=100, key=f"tiltak_neste_{block_id}")

        # Remove button
        if st.button("Fjern", key=f"remove_{block_id}"):
            remove_block(block_id)

# Add new KPI block
if st.button("➕ Legg til KPI"):
    st.session_state.kpi_blocks.append(str(uuid.uuid4()))

# Generate summaries
if st.button("📋 Vis oppsummering"):
    heading = "Oppfølging"
    if name:
        heading += f" – {name}"
    if dato:
        heading += f" – {dato.strftime('%d.%m.%Y')}"

    st.subheader(heading)

    full_summary = f"{heading}\n\n🧾 FULL OPPSUMMERING\n"
    short_summary = "\n📌 **KORT OPPSUMMERING**\n"

    for i, block_id in enumerate(st.session_state.kpi_blocks):
        kpi = st.session_state.get(f"kpi_{block_id}", "")
        tiltak_sist = st.session_state.get(f"tiltak_sist_{block_id}", "")
        status_sist = st.session_state.get(f"status_sist_{block_id}", "")
        status_no = st.session_state.get(f"status_no_{block_id}", "")
        fungerte = st.session_state.get(f"fungerte_{block_id}", "")
        mal_neste = st.session_state.get(f"mal_neste_{block_id}", "")
        tiltak_neste = st.session_state.get(f"tiltak_neste_{block_id}", "")

        full_summary += (
            f"\n### KPI {i+1}\n"
            f"**KPI**  \n{kpi}\n\n"
            f"**Tiltak sist**  \n{tiltak_sist}\n\n"
            f"**Status sist**  \n{status_sist}\n\n"
            f"**Status no**  \n{status_no}\n\n"
            f"**Kva fungerte / fungerte ikkje**  \n{fungerte}\n\n"
            f"**Mål til neste gang**  \n{mal_neste}\n\n"
            f"**Tiltak til neste gang**  \n{tiltak_neste}\n\n"
            f"---\n"
        )

        short_summary += (
            f"\n**{i+1}. {kpi}**\n\n"
            f"🎯 **Mål til neste gang**  \n{mal_neste}\n\n"
            f"🛠️ **Tiltak til neste gang**  \n{tiltak_neste}\n\n"
            f"---\n"
        )

    combined_summary = full_summary + "\n\n" + short_summary

    st.markdown("### 📋 Kopier og lim inn i e-post")
    st.text_area("Trykk Ctrl+C for å kopiere", combined_summary.strip(), height=600)
