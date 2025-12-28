import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class FeatureEngineer:
    def __init__(self):
        self.num_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
        self.cat_cols = ["Contract", "PaymentMethod"]
        self.scaler = StandardScaler()
        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        self.fitted = False
        self.feature_names_ = None

    def fit_transform(self, rows: list):
        df = pd.DataFrame(rows)

        # Target
        y = df["Churn"].astype(int).values

        # Drop non-features
        X_num = df[self.num_cols]
        X_cat = df[self.cat_cols]

        # Fit transforms
        Xn = self.scaler.fit_transform(X_num)
        Xc = self.encoder.fit_transform(X_cat)

        # Feature names
        cat_names = self.encoder.get_feature_names_out(self.cat_cols)
        self.feature_names_ = self.num_cols + list(cat_names)

        self.fitted = True
        X = np.hstack([Xn, Xc])
        return X, y

    def transform(self, rows: list):
        if not self.fitted:
            raise RuntimeError("FeatureEngineer not fitted")

        df = pd.DataFrame(rows)
        Xn = self.scaler.transform(df[self.num_cols])
        Xc = self.encoder.transform(df[self.cat_cols])
        X = np.hstack([Xn, Xc])
        return X
