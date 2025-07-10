import streamlit as st
import joblib
import numpy as np

pemanis_gif_url = 'pemanis.gif'
model = joblib.load('knn_uts.pkl')

st.title("Heart Disease Risk Classifier 💓")
# st.image(pemanis_gif_url, caption="Bocchi The Rock is here!", use_column_width=True)

# Binary inputs (0 = No, 1 = Yes)
options_map = {"Tidak": 0, "Ya": 1}

HighBP = st.selectbox("Tekanan Darah Tinggi?", options=list(options_map.keys()), index=0)
HighBP = options_map[HighBP]

HighChol = st.selectbox("Kolesterol Tinggi?", options=list(options_map.keys()), index=0)
HighChol = options_map[HighChol]

CholCheck = st.selectbox("Pernah Tes Kolesterol?", options=list(options_map.keys()), index=0)
CholCheck = options_map[CholCheck]

BMI = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=100.0, value=25.0)

Smoker = st.selectbox("Merokok?", options=list(options_map.keys()), index=0)
Smoker = options_map[Smoker]

Stroke = st.selectbox("Pernah Stroke?", options=list(options_map.keys()), index=0)
Stroke = options_map[Stroke]

Diabetes = st.selectbox("Punya Diabetes?", options=list(options_map.keys()), index=0)
Diabetes = options_map[Diabetes]

PhysActivity = st.selectbox("Aktif secara fisik?", options=list(options_map.keys()), index=0)
PhysActivity = options_map[PhysActivity]

Fruits = st.selectbox("Konsumsi buah tiap hari?", options=list(options_map.keys()), index=0)
Fruits = options_map[Fruits]

Veggies = st.selectbox("Konsumsi sayur tiap hari?", options=list(options_map.keys()), index=0)
Veggies = options_map[Veggies]

HvyAlchoholCons = st.selectbox("Konsumsi alkohol berlebihan?", options=list(options_map.keys()), index=0)
HvyAlchoholCons = options_map[HvyAlchoholCons]

AnyHealthcare = st.selectbox("Punya akses layanan kesehatan?", options=list(options_map.keys()), index=0)
AnyHealthcare = options_map[AnyHealthcare]
GenHlth = st.slider("Kesehatan secara umum (1 = sehat, 5 = buruk)", 1, 5, 3)
MentHlth = st.slider("Berapa hari terganggu mental? (0-30)", 0, 30, 0)
PhysHlth = st.slider("Berapa hari terganggu fisik? (0-30)", 0, 30, 0)

DiffWalk = st.selectbox("Kesulitan berjalan?", options=list(options_map.keys()), index=0)
DiffWalk = options_map[DiffWalk]

Sex = st.selectbox("Jenis Kelamin (0 = Perempuan, 1 = Laki-laki)", options=list(options_map.keys()), index=0)
Sex = options_map[Sex]

Age = st.slider("Umur", 1, 120, 30)

# button to trigger prediction
if st.button("Prediksi"):
    input_data = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Diabetes,
                            PhysActivity, Fruits, Veggies, HvyAlchoholCons, AnyHealthcare,
                            GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Risiko tinggi terkena penyakit jantung!")
    else:
        st.success("💚 Risiko rendah terkena penyakit jantung.")
