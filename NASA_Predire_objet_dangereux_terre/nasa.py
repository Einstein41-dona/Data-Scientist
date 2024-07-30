import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle
import plotly.express as px
import streamlit as st

# un title pour l'appli
st.title("Prediction de l'objet dangereux proche de la terre")
#author
st.subheader('Author:Eric KOULODJI')

#chargement du model
with open ('Random_forest_pkl', 'rb') as file:
    Model = pickle.load(file)
    
