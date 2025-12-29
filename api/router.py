from fastapi import APIRouter
from api.v1.health import router as health_router
from api.v1.predict import router as predict_router

router = APIRouter()

router.include_router(health_router, tags=["Health"])
router.include_router(predict_router, tags=["Prediction"])
