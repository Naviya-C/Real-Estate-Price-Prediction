from fastapi import FastAPI
from model import load_model, predict
from schemas import PredictRequest, PredictionResponse

app = FastAPI()
model = load_model()

@app.post("/predict", response_model = PredictionResponse)
def make_prediction(request: PredictRequest):
    prediction = predict(model, request.data)
    return {"Prediction" : prediction}