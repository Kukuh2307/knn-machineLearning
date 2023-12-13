import pickle
import streamlit as st

# Model = '/home/kisawa16/Documents/KULIAH/MACHINE LEARNING/UTS/KNN/knn_model.pkl'
knnModel = pickle.load(open('knn_model.sav', 'rb'))

st.title('KNN - Prediksi Kualitas Air')

col1, col2 = st.columns(2)
with col1:
    almunium = st.text_input('Masukkan kadar almunium')
    amonia = st.text_input('Masukkan kadar amonia')
    arsenic = st.text_input('Masukkan kadaar arsenic')
    barium = st.text_input('Masukkan kadar barium')
    cadmium = st.text_input('Masukkan kadar cadmium')
    chloramine = st.text_input('Masukkan kadar chloramine')
    chromium = st.text_input('Masukkan kadar chromium')
    copper = st.text_input('Masukkan kadar copper')
    flouride = st.text_input('Masukkan kadar flouride')
    bacteria = st.text_input('Masukkan kadar bacteria')

with col2:
    viruses = st.text_input('Masukkan kadar viruses')
    lead = st.text_input('Masukkan kadar lead')
    nitrates = st.text_input('Masukkan kadar nitrates')
    nitrites = st.text_input('Masukkan kadar nitrites')
    mercury = st.text_input('Masukkan kadar mercury')
    perchlorate = st.text_input('Masukkan kadar perchlorate')
    radium = st.text_input('Masukkan kadar radium')
    selenium = st.text_input('Masukkan kadar selenium')
    silver = st.text_input('Masukkan kadar silver')
    uranium = st.text_input('Masukkan kadar uranium')

if almunium and amonia and arsenic and barium and cadmium and chloramine and chromium and copper and flouride and bacteria and viruses and lead and nitrates and mercury and perchlorate and radium and selenium and silver and uranium:
    input_data = [
        float(almunium), float(amonia), float(barium), float(cadmium), float(chloramine), float(chromium), float(copper), float(flouride), float(bacteria), float(
            viruses), float(lead), float(nitrates), float(mercury), float(perchlorate), float(radium), float(selenium), float(silver), float(uranium)
    ]

    water_status = ''
    if st.button('Kalkulasi hasil Prediksi kandungan air'):
        water_predict = knnModel.predict([input_data])

        if water_predict[0] == 1:
            water_status = "Kandungan air aman"
        else:
            water_status = "Kandungan air tidak aman"

    st.success(water_status)
else:
    st.warning("Masukkan semua nilai atribut sebelum melihat hasil prediksi")
