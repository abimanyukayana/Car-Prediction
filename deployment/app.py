# Import Library
import streamlit as st

# Import halaman streamlit yang sudah dibuat
import deployment.eda as eda
import deployment.prediction_model as model

# Tombol navigasi di sidebar
navigasi = st.sidebar.selectbox('Pilih Halaman:', ('Model Prediksi', 'EDA'))

# Navigasi antar halaman
if navigasi == 'Model Prediksi':
    model.run()
else:
    eda.run()