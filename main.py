from database.query import fetch

hello = fetch("SELECT * FROM TelecoChurnData")

print(hello)