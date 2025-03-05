import streamlit as st
import requests
import json

# Définir les URL de l'API en fonction du choix
LOCAL_API_URL = "http://127.0.0.1:8000/predict"
DOCKER_AWS_URL = "http://34.229.62.59:80/predict"

# Interface utilisateur Streamlit
st.title("Test de l'API de prédiction de solvabilité")
st.write("Entrez les caractéristiques du client pour obtenir une prédiction :")

# Choix de l'application (API)
api_choice = st.sidebar.selectbox("Type de test de l'API", ["Local", "Docker/AWS"])

# Sélectionner l'URL en fonction de l'option choisie
if api_choice == "Local":
    api_url = LOCAL_API_URL
else:
    api_url = DOCKER_AWS_URL

# Création d'un formulaire pour saisir les données d'entrée
data_input = st.text_area("Données d'entrée (format JSON)", "{}")

# Custom CSS for button color
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

predict_button = st.button("Prédire")

if predict_button:
    try:
        # Convertir le texte en dictionnaire
        input_data = json.loads(data_input)
        
        # Envoyer la requête à l'API sélectionnée
        response = requests.post(api_url, json=input_data)
        
        if response.status_code == 200:
            prediction = response.json()
            st.write("C'est quoi le statut financier du client ?\n")
            st.success(f"Résultat : {prediction['Prédiction']}")
        else:
            st.error(f"Erreur API : {response.status_code}, {response.text}")
    except Exception as e:
        st.error(f"Erreur de traitement : {str(e)}")
