import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd
import pickle

# un titre 
st.title("Application pour prédire le prix d'un appartement")
#auteur
st.subheader("Auteur:", "Eric KOULODJI")
#chargement du modele

with open('Gradient_boosting.pkl', 'rb') as file:
    model = pickle.load(file)

def get_predictions(MSSubClass, LotFrontage, LotArea, ScreenPorch, YrSold, MiscVal, MoSold, PoolArea):
    input_data = np.array([MSSubClass, LotFrontage, LotArea, ScreenPorch, YrSold, MiscVal,
                           MoSold, PoolArea])
    prediction = model.predict(input_data.reshape(-1, 1))
    return prediction[0]
   
#entree utilisateur
MSSubClass = st.number_input('MSSubClass', min_value=20.0, max_value=190.0)
LotFrontage = st.number_input('LotFrontage', min_value=21.0, max_value=313.0)
LotArea = st.number_input('LotArea', min_value=20.0, max_value=190.0)
ScreenPorch = st.number_input('ScreenPorch', min_value=20.0, max_value=190.0)
YrSold = st.number_input('YrSold', min_value=2001, max_value=2024)
MiscVal = st.number_input('MiscVal', min_value=20.0, max_value=190.0)
MoSold = st.number_input('MoSold', min_value=1, max_value=12)
PoolArea = st.number_input('PoolArea', min_value=20.0, max_value=190.0)

if st.button('Predire'):
    prediction = get_predictions(MSSubClass, LotFrontage, LotArea, 
                                 ScreenPorch, YrSold, MiscVal, 
                                 MoSold, PoolArea)
    st.write(f"Le prix de l'appartement est: {prediction}")