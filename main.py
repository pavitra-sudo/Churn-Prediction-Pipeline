from database.query import fetch
from pipeline.data_validation import validate_data
from pipeline.data_cleaning import clean_data
from pipeline.feature_engineering import FeatureEngineer
from pipeline.train_model import train_and_save

# Phase 1
rows = fetch("SELECT * FROM TelecoChurnData")

# Phase 2
validate_data(rows)

# Phase 3
cleaned = clean_data(rows)

# Phase 4
fe = FeatureEngineer()
X, y = fe.fit_transform(cleaned)

# Phase 5
metrics = train_and_save(X, y, fe)
