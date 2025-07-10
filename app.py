import streamlit as st
import joblib
import numpy as np

pemanis_gif_url = 'pemanis.gif'
model = joblib.load('knn_uts.pkl')

st.title("Heart Disease Risk Classifier 💓")
# st.image(pemanis_gif_url, caption="Bocchi The Rock is here!", use_column_width=True)

# st.markdown("---")
# st.markdown("### 📋 Silakan isi formulir berikut untuk mengetahui risiko penyakit jantung Anda")
# st.markdown("*Semua pertanyaan wajib diisi untuk mendapatkan hasil yang akurat*")

# Binary inputs (0 = No, 1 = Yes)
options_map = {"Tidak": 0, "Ya": 1}

# Binary inputs (0 = No, 1 = Yes)
options_map = {"Tidak": 0, "Ya": 1}

# Section 1: Informasi Dasar
st.markdown("### 👤 Informasi Dasar")
col1, col2 = st.columns(2)

with col1:
    Age = st.slider("Umur", 1, 120, 30)
    Sex = st.selectbox("Jenis Kelamin", options=["Perempuan", "Laki-laki"], index=0)
    Sex = 0 if Sex == "Perempuan" else 1

with col2:
    GenHlth = st.slider("Kesehatan secara umum", 1, 5, 3, help="1 = Sangat sehat, 5 = Sangat buruk")
    BMI = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=100.0, value=25.0, help="Indeks Massa Tubuh - Normal: 18.5-24.9")

# Section 2: Riwayat Medis
st.markdown("---")
st.markdown("### 🏥 Riwayat Medis")
col3, col4 = st.columns(2)

with col3:
    HighBP = st.selectbox("Tekanan Darah Tinggi?", options=list(options_map.keys()), index=0)
    HighBP = options_map[HighBP]
    
    HighChol = st.selectbox("Kolesterol Tinggi?", options=list(options_map.keys()), index=0)
    HighChol = options_map[HighChol]
    
    CholCheck = st.selectbox("Pernah Tes Kolesterol?", options=list(options_map.keys()), index=0)
    CholCheck = options_map[CholCheck]
    
    Stroke = st.selectbox("Pernah Stroke?", options=list(options_map.keys()), index=0)
    Stroke = options_map[Stroke]

with col4:
    Diabetes = st.selectbox("Punya Diabetes?", options=list(options_map.keys()), index=0)
    Diabetes = options_map[Diabetes]
    
    DiffWalk = st.selectbox("Kesulitan Berjalan?", options=list(options_map.keys()), index=0)
    DiffWalk = options_map[DiffWalk]
    
    AnyHealthcare = st.selectbox("Punya Akses Layanan Kesehatan?", options=list(options_map.keys()), index=0)
    AnyHealthcare = options_map[AnyHealthcare]

# Section 3: Gaya Hidup
st.markdown("---")
st.markdown("### 🚭 Gaya Hidup")
col5, col6 = st.columns(2)

with col5:
    Smoker = st.selectbox("Merokok?", options=list(options_map.keys()), index=0)
    Smoker = options_map[Smoker]
    
    PhysActivity = st.selectbox("Aktif Secara Fisik?", options=list(options_map.keys()), index=0, help="Olahraga atau aktivitas fisik rutin")
    PhysActivity = options_map[PhysActivity]
    
    HvyAlchoholCons = st.selectbox("Konsumsi Alkohol Berlebihan?", options=list(options_map.keys()), index=0)
    HvyAlchoholCons = options_map[HvyAlchoholCons]

with col6:
    Fruits = st.selectbox("Konsumsi Buah Tiap Hari?", options=list(options_map.keys()), index=0)
    Fruits = options_map[Fruits]
    
    Veggies = st.selectbox("Konsumsi Sayur Tiap Hari?", options=list(options_map.keys()), index=0)
    Veggies = options_map[Veggies]

# Section 4: Kesehatan Mental & Fisik
st.markdown("---")
st.markdown("### 🧠 Kesehatan Mental & Fisik (30 hari terakhir)")
col7, col8 = st.columns(2)

with col7:
    MentHlth = st.slider("Berapa hari terganggu mental?", 0, 30, 0, help="Hari dengan masalah kesehatan mental")

with col8:
    PhysHlth = st.slider("Berapa hari terganggu fisik?", 0, 30, 0, help="Hari dengan masalah kesehatan fisik")

# Prediction Button and Results
st.markdown("---")
st.markdown("### 🔮 Hasil Prediksi")

# Center the button
col_center = st.columns([1, 2, 1])
with col_center[1]:
    predict_button = st.button("🔍 Prediksi Risiko Penyakit Jantung", type="primary", use_container_width=True)

if predict_button:
    # Show loading spinner
    with st.spinner('Menganalisis data kesehatan Anda...'):
        input_data = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Diabetes,
                                PhysActivity, Fruits, Veggies, HvyAlchoholCons, AnyHealthcare,
                                GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age]])
        
        prediction = model.predict(input_data)

    # Display results with better formatting
    st.markdown("### Hasil Analisis:")
    
    if prediction[0] == 1:
        st.error("⚠️ **RISIKO TINGGI** terkena penyakit jantung!")
        st.markdown("""
        **Rekomendasi:**
        - 🏥 Segera konsultasi dengan dokter
        - 💊 Lakukan pemeriksaan kesehatan menyeluruh
        - 🏃‍♂️ Tingkatkan aktivitas fisik
        - 🥗 Perbaiki pola makan
        - 🚭 Hindari merokok dan alkohol
        """)
    else:
        st.success("💚 **RISIKO RENDAH** terkena penyakit jantung.")
        st.markdown("""
        **Pertahankan gaya hidup sehat:**
        - ✅ Terus jaga pola makan seimbang
        - ✅ Rutin berolahraga
        - ✅ Pemeriksaan kesehatan berkala
        - ✅ Hindari stress berlebihan
        """)
    
    st.info("💡 **Catatan:** Hasil ini hanya prediksi berdasarkan data yang diinput. Untuk diagnosis yang akurat, selalu konsultasikan dengan tenaga medis profesional.")
