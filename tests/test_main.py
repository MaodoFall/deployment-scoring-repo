from fastapi.testclient import TestClient
from api_rest.main import app  #
import pandas as pd
import re
from sklearn.preprocessing import StandardScaler

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Prédiction de la solvabilité du client"}


def test_predict_client_solvable(data):
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    prediction = response.json()
    assert "Prédiction" in prediction
    assert prediction["Prédiction"] in ["Client solvable", "Client non solvable"]
