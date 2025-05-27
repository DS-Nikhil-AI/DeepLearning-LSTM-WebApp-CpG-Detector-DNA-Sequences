import streamlit as st
from flask_app.model_utils import load_model, predict

st.title("DNA Sequence Predictor")
with st.form("DNA_Form_Prediction"):
    sequence = st.text_input("Enter DNA Sequence (e.g., NCACANNTNCGGAGGCGNA):")

    model_type = st.selectbox("Select Model Type", ("Fixed-Length (No Padding)", "Variable-Length (With Padding)"))
    submitted=False
    submitted = st.form_submit_button("Submit")

    if sequence and submitted:
        if model_type == "Fixed-Length (No Padding)":
            model = load_model("models/128dim_model.pkl")
            result = predict(model, sequence, pad=False)
        else:
            model = load_model("models/128dim_padding_model.pt")
            result = predict(model, sequence, pad=True, max_len=20)
        st.write(f"Model Output: `{result:.4f}`")

        
