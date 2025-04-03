import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_price(latitude, longitude):
    features = np.array([[latitude, longitude]])
    return model.predict(features)[0]

st.title("🏡 Stima del Prezzo Immobili a Sindian, Taiwan")
st.write("Inserisci la latitudine e la longitudine per ottenere una stima del prezzo al metro quadro.")
latitude = st.number_input("Latitudine", min_value=24.0, max_value=25.0, value=24.5, step=0.001)
longitude = st.number_input("Longitudine", min_value=121.4, max_value=121.7, value=121.5, step=0.001)

if st.button("Calcola Prezzo"):
    price = predict_price(latitude, longitude)
    st.success(f"Il prezzo stimato è **{price:.2f} unità monetarie per m²**")