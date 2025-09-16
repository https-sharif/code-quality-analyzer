import streamlit as st
from predict import predict_code_quality
import tempfile
import os

st.title("Code Quality Predictor")
st.write("Paste your Python or JavaScript code below and press Predict.")

code_input = st.text_area("Code", height=300)

if st.button("Predict"):
    if not code_input.strip():
        st.warning("Please paste some code first.")
    else:
        with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp:
            tmp.write(code_input)
            temp_filepath = tmp.name
        
        try:
            cluster, label = predict_code_quality(temp_filepath)
            
            if label.lower() == "good":
                st.success(f"Predicted code quality: {label}")
            elif label.lower() == "average":
                st.warning(f"Predicted code quality: {label}")
            else:
                st.error(f"Predicted code quality: {label}")
        finally:
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)
