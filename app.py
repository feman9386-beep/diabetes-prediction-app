import streamlit as st
import pickle
from pathlib import Path

st.set_page_config(page_title="Diabetes Prediction App", page_icon="🩺")

st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient information below to predict the diabetes outcome.")

MODEL_PATH = Path(__file__).parent / "logistic_regression_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
st.subheader("Patient Information")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0, step=1)
    glucose = st.number_input("Glucose", min_value=0.0, max_value=300.0, value=120.0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=70.0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0.0, max_value=100.0, value=20.0)

with col2:
    insulin = st.number_input("Insulin", min_value=0.0, max_value=900.0, value=80.0)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)

if st.button("Predict Diabetes", type="primary"):
    data = [[pregnancies, glucose, blood_pressure, skin_thickness,
             insulin, bmi, diabetes_pedigree, age]]

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("Prediction: Diabetes")
    else:
        st.success("Prediction: No Diabetes")

st.caption("For educational/demo purposes only. This is not a medical diagnosis.")
