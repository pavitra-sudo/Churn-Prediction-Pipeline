from database.query import fetch
from pipeline.data_validation import validate_data

rows = fetch("SELECT * FROM TelecoChurnData")

validate_data(rows)

