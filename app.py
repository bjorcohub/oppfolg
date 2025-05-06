if st.button("📋 Vis oppsummering"):
    heading = "Oppfølging"
    if name:
        heading += f" – {name}"
    if dato:
        heading += f" – {dato.strftime('%d.%m.%Y')}"
    st.subheader(heading)

    full_summary = f"{heading}\n\n🧾 FULL OPPSUMMERING\n"
    short_summary = "📌 KORT OPPSUMMERING\n"

    for i, block in enumerate(st.session_state.kpi_blocks):
        kpi = st.session_state.get(f"kpi_{i}", "")
        tiltak_sist = st.session_state.get(f"tiltak_sist_{i}", "")
        status_sist = st.session_state.get(f"status_sist_{i}", "")
        status_no = st.session_state.get(f"status_no_{i}", "")
        fungerte = st.session_state.get(f"fungerte_{i}", "")
        mal_neste = st.session_state.get(f"mal_neste_{i}", "")
        tiltak_neste = st.session_state.get(f"tiltak_neste_{i}", "")

        full_summary += f"""KPI {i+1}:
**- KPI:** {kpi}
**- Tiltak sist:** {tiltak_sist}
**- Status sist:** {status_sist}
**- Status no:** {status_no}
**- Kva fungerte / fungerte ikkje:** {fungerte}
**- Mål til neste gang:** {mal_neste}
**- Tiltak til neste gang:** {tiltak_neste}
---
"""

        short_summary += f"""\n{i+1}. {kpi}
🎯 Mål:
{mal_neste}
🛠️ Tiltak:
{tiltak_neste}
"""

    # Display summaries
    st.markdown("### 🧾 Full oppsummering")
    st.markdown(full_summary)
    st.markdown("### 📌 Kort oppsummering")
    st.text(short_summary)

    # Combined output
    combined_summary = full_summary + "\n\n" + short_summary

    st.markdown("### 📋 Kopier og lim inn i e-post")
    st.text_area("Trykk Ctrl+C for å kopiere", combined_summary, height=600)
