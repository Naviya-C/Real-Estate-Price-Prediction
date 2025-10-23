from fastapi import FastAPI
from model import load_model, predict
from schemas import PredictRequest, PredictionResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500"],
    allow_credentials = True,
    allow_methods = [""],
    allow_header = [""],
)

@app.post("/predict", response_model = PredictionResponse)
def make_prediction(request: PredictRequest):
    prediction = predict(model, request.data)
    return {"Prediction" : prediction}