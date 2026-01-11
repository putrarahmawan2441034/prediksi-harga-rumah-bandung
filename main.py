from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

# =========================
# LOAD MODEL BANDUNG
# =========================
model = joblib.load("bandung_house_price_model.pkl")

app = FastAPI(
    title="Bandung House Price Prediction API",
    description="Prediksi harga rumah di Kota Bandung berdasarkan dataset Kaggle",
    version="1.0"
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# INPUT SCHEMA (SESUAI DATASET)
# =========================
class HouseData(BaseModel):
    luas_tanah: float        # m²
    luas_bangunan: float    # m²
    kamar_tidur: int
    kamar_mandi: int

# =========================
# PREDICTION ENDPOINT
# =========================
@app.post("/predict")
def predict_house_price(data: HouseData):
    input_data = np.array([[
        data.luas_tanah,
        data.luas_bangunan,
        data.kamar_tidur,
        data.kamar_mandi
    ]])

    prediction = model.predict(input_data)

    return {
        "predicted_price_miliar": float(prediction[0]),
        "note": "Harga berdasarkan pola data rumah di Kota Bandung"
    }

# Run with:
# uvicorn main:app --reload
