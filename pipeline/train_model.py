import json
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

def train_and_save(X, y, feature_engineer):
    # 1️⃣ Train / validation split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 2️⃣ Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 3️⃣ Evaluate
    y_pred = model.predict(X_val)
    y_prob = model.predict_proba(X_val)[:, 1]

    metrics = {
        "accuracy": round(accuracy_score(y_val, y_pred), 4),
        "roc_auc": round(roc_auc_score(y_val, y_prob), 4),
        "samples": len(y)
    }

    # 4️⃣ Save artifacts
    joblib.dump(model, "models/churn_model.pkl")
    joblib.dump(feature_engineer, "models/feature_engineer.pkl")

    with open("models/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("🤖 Phase 5 complete — Model trained & saved")
    print("📊 Metrics:", metrics)

    return metrics
