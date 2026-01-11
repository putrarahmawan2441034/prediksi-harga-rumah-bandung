import pandas as pd
import joblib
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

print("🚀 Training dimulai")

df = pd.read_csv("dataset/harga_rumah_bandung.csv", header=None)

df.columns = [
    "tipe",
    "kategori",
    "harga_text",
    "cicilan",
    "deskripsi",
    "lokasi",
    "kamar_tidur",
    "kamar_mandi",
    "harga_miliar",
    "luas_tanah",
    "luas_bangunan"
]

# ======================
# CLEANING
# ======================
def extract_number(text):
    if pd.isna(text):
        return None
    nums = re.findall(r"\d+\.?\d*", str(text).replace(",", "."))
    return float(nums[0]) if nums else None

df["luas_tanah"] = df["luas_tanah"].apply(extract_number)
df["luas_bangunan"] = df["luas_bangunan"].apply(extract_number)
df["kamar_tidur"] = pd.to_numeric(df["kamar_tidur"], errors="coerce")
df["kamar_mandi"] = pd.to_numeric(df["kamar_mandi"], errors="coerce")

# HARGA DALAM MILIAR
df["harga"] = df["harga_text"].apply(extract_number)

# Filter nilai tidak masuk akal
df = df[
    (df["harga"] < 50) &     # max 50 Miliar
    (df["luas_tanah"] < 500) &
    (df["luas_bangunan"] < 500)
]

df = df.dropna()

print("📊 Data final:", df.shape)

# ======================
# TRAIN
# ======================
X = df[["luas_tanah", "luas_bangunan", "kamar_tidur", "kamar_mandi"]]
y = df["harga"]   # sudah dalam MILIAR

model = Pipeline([
    ("scaler", StandardScaler()),
    ("lr", LinearRegression())
])

model.fit(X, y)

joblib.dump(model, "bandung_house_price_model.pkl")
print("✅ MODEL DISIMPAN")
