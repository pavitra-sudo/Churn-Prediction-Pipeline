def clean_data(rows: list) -> list:
    cleaned = []

    for row in rows:
        r = row.copy()

        # 1) Numeric fixes
        for col in ["tenure", "MonthlyCharges", "TotalCharges"]:
            v = r.get(col)
            if v in ("", " ", None):
                r[col] = 0.0
            else:
                r[col] = float(v)

        # 2) Target normalization
        if r.get("Churn") == "Yes":
            r["Churn"] = 1
        elif r.get("Churn") == "No":
            r["Churn"] = 0

        # 3) String hygiene
        for k, v in r.items():
            if isinstance(v, str):
                r[k] = v.strip()

        cleaned.append(r)

    print("🧹 Phase 3: Data cleaning completed")
    return cleaned
