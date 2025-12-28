from database.query import fetch
from pipeline.data_validation import validate_data
from pipeline.data_cleaning import clean_data

rows = fetch("SELECT * FROM TelecoChurnData")

validate_data(rows)          # Phase 2 gate
cleaned_rows = clean_data(rows)



