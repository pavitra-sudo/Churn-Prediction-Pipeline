from database.query import fetch
from pipeline.data_validation import validate_data
from pipeline.data_cleaning import clean_data
from pipeline.feature_engineering import FeatureEngineer

rows = fetch("SELECT * FROM TelecoChurnData")

validate_data(rows)              # Phase 2
cleaned = clean_data(rows)       # Phase 3

fe = FeatureEngineer()
X, y = fe.fit_transform(cleaned)

print("⚙️ Phase 4 done")
print("X shape:", X.shape)
print("y distribution:", {0: int((y==0).sum()), 1: int((y==1).sum())})
