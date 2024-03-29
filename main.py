import datetime
from pydantic import BaseModel, Field
from fastapi import Form
from fastapi.responses import HTMLResponse, FileResponse
from ms import app
from ms.functions import get_model_response

model_name = "Breast Cancer Wisconsin (Diagnostic)"
version = "v1.0.0"


class Input(BaseModel):
    concavity_mean: float = Field(..., gt=0)
    concave_points_mean: float = Field(..., gt=0)
    perimeter_se: float = Field(..., gt=0)
    area_se: float = Field(..., gt=0)
    texture_worst: float = Field(..., gt=0)
    area_worst: float = Field(..., gt=0)

    class Config:
        schema_extra = {
            "concavity_mean": 0.3001,
            "concave_points_mean": 0.1471,
            "perimeter_se": 8.589,
            "area_se": 153.4,
            "texture_worst": 17.33,
            "area_worst": 2019.0,
        }


class Output(BaseModel):
    label: str
    prediction: int


@app.get("/")
async def get_index():
    return FileResponse("./static/predict.html")


@app.get("/model-info", response_class=HTMLResponse)
async def model_info():
    """Return model information, version, how to call"""
    return f"<h2>Model Name: {model_name}</h2><h2>Version: {version}</h2>"


@app.get("/health")
async def service_health():
    """Return service health"""
    return {"ok"}


@app.post("/predict", response_model=Output)
async def model_predict(input: Input):
    """Predict with input"""
    response = get_model_response(input)
    return response
