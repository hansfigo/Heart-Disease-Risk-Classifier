import streamlit as st
import joblib
import numpy as np

model = joblib.load('knn_uts.pkl')

st.title("Heart Disease Risk Classifier 💓")

# Binary inputs (0 = No, 1 = Yes)
HighBP = st.selectbox("Tekanan Darah Tinggi?", [0, 1])
HighChol = st.selectbox("Kolesterol Tinggi?", [0, 1])
CholCheck = st.selectbox("Pernah Tes Kolesterol?", [0, 1])
BMI = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=100.0, value=25.0)
Smoker = st.selectbox("Merokok?", [0, 1])
Stroke = st.selectbox("Pernah Stroke?", [0, 1])
Diabetes = st.selectbox("Punya Diabetes?", [0, 1])
PhysActivity = st.selectbox("Aktif secara fisik?", [0, 1])
Fruits = st.selectbox("Konsumsi buah tiap hari?", [0, 1])
Veggies = st.selectbox("Konsumsi sayur tiap hari?", [0, 1])
HvyAlchoholCons = st.selectbox("Konsumsi alkohol berlebihan?", [0, 1])
AnyHealthcare = st.selectbox("Punya akses layanan kesehatan?", [0, 1])
GenHlth = st.slider("Kesehatan secara umum (1 = sehat, 5 = buruk)", 1, 5, 3)
MentHlth = st.slider("Berapa hari terganggu mental? (0-30)", 0, 30, 0)
PhysHlth = st.slider("Berapa hari terganggu fisik? (0-30)", 0, 30, 0)
DiffWalk = st.selectbox("Kesulitan berjalan?", [0, 1])
Sex = st.selectbox("Jenis Kelamin (0 = Perempuan, 1 = Laki-laki)", [0, 1])
Age = st.slider("Umur", 1, 120, 30)

# Tombol prediksi
if st.button("Prediksi"):
    input_data = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Diabetes,
                            PhysActivity, Fruits, Veggies, HvyAlchoholCons, AnyHealthcare,
                            GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Risiko tinggi terkena penyakit jantung!")
    else:
        st.success("💚 Risiko rendah terkena penyakit jantung.")
