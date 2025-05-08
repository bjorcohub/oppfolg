import streamlit as st
from datetime import date

st.set_page_config(page_title="KPI Skjema", layout="centered")
st.title("📝 KPI Skjema")

# Initialize session state
if "kpi_blocks" not in st.session_state:
    st.session_state.kpi_blocks = [0]

# Name and date input
name = st.text_input("Navn")
dato = st.date_input("Dato", value=date.today())

def remove_block(index):
    st.session_state.to_remove_index = index

# Render KPI blocks
for i, block in enumerate(st.session_state.kpi_blocks):
    with st.container():
        st.markdown(f"### KPI {i+1}")
        kpi = st.text_area("KPI", height=50, key=f"kpi_{i}")
        tiltak_sist = st.text_area("Tiltak sist", height=100, key=f"tiltak_sist_{i}")
        status_sist = st.text_area("Status sist", height=100, key=f"status_sist_{i}")
        status_no = st.text_area("Status no", height=100, key=f"status_no_{i}")
        fungerte = st.text_area("Kva fungerte / fungerte ikkje", height=150, key=f"fungerte_{i}")
        mal_neste = st.text_area("Mål til neste gang", height=100, key=f"mal_neste_{i}")
        tiltak_neste = st.text_area("Tiltak til neste gang", height=100, key=f"tiltak_neste_{i}")

        # Remove button
        if st.button("Fjern", key=f"remove_{i}"):
            remove_block(i)

# Safe block removal AFTER widgets render
if "to_remove_index" in st.session_state:
    idx = st.session_state.to_remove_index
    if 0 <= idx < len(st.session_state.kpi_blocks):
        st.session_state.kpi_blocks.pop(idx)
        for key in [
            f"kpi_{idx}", f"tiltak_sist_{idx}", f"status_sist_{idx}", f"status_no_{idx}",
            f"fungerte_{idx}", f"mal_neste_{idx}", f"tiltak_neste_{idx}"
        ]:
            st.session_state.pop(key, None)
    del st.session_state.to_remove_index
    st.experimental_rerun()

# Add button
if st.button("➕ Legg til KPI"):
    st.session_state.kpi_blocks.append(len(st.session_state.kpi_blocks))

# Generate summaries
if st.button("📋 Vis oppsummering"):
    heading = "Oppfølging"
    if name:
        heading += f" – {name}"
    if dato:
        heading += f" – {dato.strftime('%d.%m.%Y')}"

    st.subheader(heading)

    full_summary = f"{heading}\n\n🧾 FULL OPPSUMMERING\n"

    for i, block in enumerate(st.session_state.kpi_blocks):
        kpi = st.session_state.get(f"kpi_{i}", "")
        tiltak_sist = st.session_state.get(f"tiltak_sist_{i}", "")
        status_sist = st.session_state.get(f"status_sist_{i}", "")
        status_no = st.session_state.get(f"status_no_{i}", "")
        fungerte = st.session_state.get(f"fungerte_{i}", "")
        mal_neste = st.session_state.get(f"mal_neste_{i}", "")
        tiltak_neste = st.session_state.get(f"tiltak_neste_{i}", "")

        full_summary += f"""
### KPI {i+1}
**KPI**  
{kpi}

**Tiltak sist**  
{tiltak_sist}

**Status sist**  
{status_sist}

**Status no**  
{status_no}

**Kva fungerte / fungerte ikkje**  
{fungerte}

**Mål til neste gang**  
{mal_neste}

**Tiltak til neste gang**  
{tiltak_neste}

---
"""

    st.markdown(full_summary)

    short_summary = f"\n📌 **TIL NESTE GANG**\n"
    for i, block in enumerate(st.session_state.kpi_blocks):
        kpi = st.session_state.get(f"kpi_{i}", "")
        mal_neste = st.session_state.get(f"mal_neste_{i}", "")
        tiltak_neste = st.session_state.get(f"tiltak_neste_{i}", "")
        short_summary += f"""
**{i+1}. {kpi}**

🎯 **Mål til neste gang**  
{mal_neste}

🛠️ **Tiltak til neste gang**  
{tiltak_neste}

---
"
