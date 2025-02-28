# main.py

# Import all packages and libraries
import pandas as pd
from fastapi import FastAPI
import pickle

# Load the pre-trained model
model = pickle.load(open("api_rest/model/lgbm_model_prod.pkl","rb"))
# Load the data
#X_test = pd.read_csv("data/data_test_feature_engine.csv",index_col=0)
#X_test = X_test.rename(columns = lambda x:re.sub("[^A-Za-z0-9_]+","",x))


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Prédiction de la solvabilité du client"}  


@app.post("/predict")
def predict(input_dict: dict):
     
    X_input = pd.DataFrame(input_dict)
    # Best threshold 
    best_threshold = 0.54
    # Make prediction
    predicted_proba_default = model.predict_proba(X_input)[:, 1]
    if predicted_proba_default >= best_threshold:
        y_val_pred = "Client non solvable"
    else:
        y_val_pred = "Client solvable"

    return {"Prédiction": y_val_pred}


