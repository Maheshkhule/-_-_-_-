# app.py
import streamlit as st
from main import run_underwriting
from pypdf import PdfReader

st.title("Insurance Underwriting Agent (AI + Risk Calculator)")

# User inputs
age = st.number_input("Enter Age:", min_value=0, max_value=120, value=25)
smoker = st.selectbox("Smoker?", ["No", "Yes"])
height = st.number_input("Height (cm):", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (kg):", min_value=10, max_value=300, value=70)

# Upload PDF
uploaded_file = st.file_uploader("Upload Medical Report (PDF)", type="pdf")
medical_text = None
if uploaded_file:
    reader = PdfReader(uploaded_file)
    medical_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            medical_text += text
    st.success("Medical report loaded.")

# Run underwriting
if st.button("Analyze"):
    with st.spinner("AI Agent is analyzing..."):
        explanation, premium = run_underwriting(age, smoker, medical_text, height, weight)
    
    st.subheader("Analysis Result")
    st.write(explanation)
    st.subheader("Estimated Premium")
    st.success(premium)