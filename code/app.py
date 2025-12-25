import streamlit as st
import pandas as pd
from predictor import DESMasterPredictor

st.set_page_config(page_title="DES Polarity Prediction System Pro", page_icon="⚗️", layout="wide")

st.title("⚗️ Deep Eutectic Solvent (DES) Intelligent Prediction System")
st.markdown("Integrated dual-cascade model of **pH Prediction** and **Polarity Prediction**.")
st.markdown("---")

# Load model
@st.cache_resource
def load_model():
    return DESMasterPredictor()

with st.sidebar:
    with st.spinner("Loading dual-model engine..."):
        predictor = load_model()
    st.success("✅ Model is ready")

tab1, tab2 = st.tabs(["🧪 Intelligent Prediction", "📂 Batch Processing"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        hba = st.text_input("HBA SMILES", "CCCC(=O)O")
        hbd = st.text_input("HBD SMILES", "C[N+](C)(C)CCO.[Cl-]")
    with col2:
        x = st.slider("HBA Molar Ratio", 0.1, 0.9, 0.75, 0.05)
        t = st.number_input("Temperature (K)", 200.0, 500.0, 313.0)
        st.info("💡 pH value will be automatically predicted by AI")

    if st.button("One-click Prediction", type="primary"):
        try:
            res = predictor.predict([{"HBA_SMILES": hba, "HBD_SMILES": hbd, "x_HBA": x, "T_K": t}])
            row = res.iloc[0]
            
            # Display automatically predicted pH
            st.metric("Predicted pH Value (AI)", f"{row['Predicted_pH']:.2f}")
            
            # Display polarity
            cols = st.columns(4)
            metrics = ["Pred_ETN", "Pred_Alpha", "Pred_Beta", "Pred_Pi_Star"]
            names = ["$E_T^N$", r"$\alpha$", r"$\beta$", "$\pi^*$"]
            for c, m, n in zip(cols, metrics, names):
                c.metric(n, f"{row[m]:.4f}")
                
        except Exception as e:
            st.error(f"Error: {e}")

with tab2:
    st.write("Upload a table containing HBA_SMILES, HBD_SMILES, x_HBA, T_K columns.")
    uploaded = st.file_uploader("Upload Excel File", type=["xlsx"])
    if uploaded and st.button("Start Batch Calculation"):
        df = pd.read_excel(uploaded)
        with st.spinner("AI is calculating pH and polarity..."):
            res = predictor.predict(df.to_dict('records'))
        st.dataframe(res)