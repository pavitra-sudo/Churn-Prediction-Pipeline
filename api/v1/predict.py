from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/predict")

# ---- Request schema ----
class ChurnRequest(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float

# ---- Response schema ----
class ChurnResponse(BaseModel):
    churn: bool
    probability: float

# ---- Prediction endpoint ----
@router.post("", response_model=ChurnResponse)
def predict_churn(data: ChurnRequest):
    # TEMP logic (will replace with real model)
    probability = 0.8 if data.tenure < 6 else 0.2
    churn = probability > 0.5

    return {
        "churn": churn,
        "probability": probability
    }
