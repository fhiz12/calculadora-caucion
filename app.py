with open("app.py", "w") as f:
    f.write('''
import streamlit as st

st.set_page_config(page_title="Calculadora de Cauciones Tomadoras", layout="centered")
st.title("📊 Calculadora de Cauciones Tomadoras")

st.markdown("""
Esta herramienta te permite calcular el costo total de una caución tomadora en función de:

- El capital recibido
- La tasa nominal anual (TNA, base 365)
- El plazo en días
- El arancel y derechos aplicado sobre el total a cancelar
""")


capital = st.number_input("💰 Capital recibido ($)", value=1_000_000.0, step=10_000.0, format="%.2f")
tasa_tna = st.number_input("📈 Tasa nominal anual (TNA %) base 365", value=40.0, step=0.5, format="%.2f")
dias = st.number_input("⏳ Plazo en días", value=7, step=1)

arancel_diario = 0.000125033334



if st.button("Calcular"):
    tasa_diaria = tasa_tna / 100 / 365
    interes_bruto = capital * tasa_diaria * dias
    monto_a_cancelar_bruto = capital + interes_bruto
    arancel_total = monto_a_cancelar_bruto * arancel_diario * dias
    total_final = monto_a_cancelar_bruto + arancel_total

        # 📌 Cálculo del CFTNA
    cftna = ((interes_bruto + arancel_total) / capital) * (365 / dias) * 100

    st.success("✅ Resultado del cálculo")
    st.markdown(f"""
    - **Capital recibido:** ${capital:,.2f}
    - **Interés bruto (TNA {tasa_tna}%):** ${interes_bruto:,.2f}
    - **Monto a cancelar (sin arancel):** ${monto_a_cancelar_bruto:,.2f}
    - **Arancel y gastos aplicados:** ${arancel_total:,.2f}
    - **🧾 Total final a cancelar:** ${total_final:,.2f}
    - **📊 CFTNA:** {cftna:.2f} %
    """)

st.markdown("""
---
💡 *By **JMSL**.*
""")

st.markdown(f"""
<style>
#wm-overlay {{
  position: fixed; inset: 0;
  display: flex; align-items: center; justify-content: center;
  pointer-events: none; z-index: 1;
}}
#wm-overlay img {{
  width: 40vw; max-width: 600px;
  opacity: 0.08; transform: rotate(-20deg);
}}
</style>
<div id="wm-overlay">
  <img src="https://www.pngfind.com/pngs/m/396-3962285_png-transparent-images-pluspng-imagenes-de-lobos-de.png" />
</div>
""", unsafe_allow_html=True)



''')
