def validate_data(rows: list):
   

    # 1️⃣ Dataset existence
    if not rows:
        raise ValueError("❌ Validation failed: No data returned from database")

    # 2️⃣ Reference schema 
    required_columns = {
        "customerID",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "Contract",
        "PaymentMethod",
        "Churn"
    }

    row_columns = set(rows[0].keys())
    missing = required_columns - row_columns
    if missing:
        raise ValueError(f"❌ Validation failed: Missing columns {missing}")

    # 3️⃣ customerID uniqueness
    customer_ids = [row["customerID"] for row in rows]
    if len(customer_ids) != len(set(customer_ids)):
        raise ValueError("❌ Validation failed: Duplicate customerID detected")

    # 4️⃣ Numeric validation (based on CSV spec)
    for row in rows:
        try:
            tenure = float(row["tenure"])
            monthly = float(row["MonthlyCharges"])
            total = float(row["TotalCharges"]) if row["TotalCharges"] not in ("", None, " ") else 0.0
        except Exception:
            raise ValueError("❌ Validation failed: Numeric conversion error")

        if tenure < 0 or monthly < 0 or total < 0:
            raise ValueError("❌ Validation failed: Negative numeric values")

    # 5️⃣ Target validation 
    allowed_churn = {"Yes", "No"}
    churn_values = set(row["Churn"] for row in rows)

    if not churn_values.issubset(allowed_churn):
        raise ValueError(f"❌ Validation failed: Invalid Churn values {churn_values}")

    if len(churn_values) != 2:
        raise ValueError("❌ Validation failed: Churn must have exactly 2 classes")

    # 6️⃣ Cardinality guardrails
    contract_vals = set(row["Contract"] for row in rows)
    payment_vals = set(row["PaymentMethod"] for row in rows)

    if len(contract_vals) > 5:
        raise ValueError("❌ Validation failed: Contract cardinality drift")

    if len(payment_vals) > 10:
        raise ValueError("❌ Validation failed: PaymentMethod cardinality drift")

    # ✅ PASSED
    print("✅ Validation passed ")
    print(f"Rows validated: {len(rows)}")
    print(f"Churn classes: {churn_values}")
