from pydantic import BaseModel
from typing import List

class PredictRequest(BaseModel):
    data : List[List[float]]

class PredictionResponse(BaseModel):
    prediction : List[float]