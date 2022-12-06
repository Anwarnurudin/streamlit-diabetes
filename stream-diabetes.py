import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title('DATA MINING PREDIKSI DIABETES')
#bagi kolom
col1,col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('input nilai Pregnancies')
    Glocouse = st.text_input ('input nilai Glocouse')
    BloodPresure = st.text_input ('input nilai BloodPresure')
    SkinThickness = st.text_input ('input nilai SkinThickness')
with col2 :
    Insulin = st.text_input ('input nilai pregnancies')
    BMI = st.text_input ('input nilai Insulin')

    DiabetesPedigreeFunction =st.text_input('input nilai diabetes Pedigree function')
    Age = st.text_input('input nilai Age')

# code untuk prediksi
diab_diagnosis =''

#tombol
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glocouse, BloodPresure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction,Age]])

    if(diab_prediction[0]==1):
        diab_diagnosis= 'Pasien terkena Diabetes'
    else:
        diab_diagnosis='Pasien terkena Diabetes'
    st.success(diab_diagnosis)