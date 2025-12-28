from database.query import fetch
from pipeline.data_validation import validate_data
from pipeline.data_cleaning import clean_data
from pipeline.feature_engineering import FeatureEngineer
from pipeline.train_model import train_and_save

def run():
    print("🚀 Starting churn ML pipeline")

    # 1) Fetch
    rows = fetch("SELECT * FROM TelecoChurnData")
    print(f"📥 Fetched {len(rows)} rows")

    # 2) Validate (gate)
    validate_data(rows)

    # 3) Clean
    cleaned = clean_data(rows)

    # 4) Features
    fe = FeatureEngineer()
    X, y = fe.fit_transform(cleaned)
    print(f"⚙️ Features ready: X={X.shape}, y={len(y)}")

    # 5) Train + save artifacts
    metrics = train_and_save(X, y, fe)

    print("✅ Pipeline finished successfully")
    print("📊 Final metrics:", metrics)

if __name__ == "__main__":
    run()
