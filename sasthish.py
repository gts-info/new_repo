
DATASETS = {
    "dataset001": [
        {"name": "Hari", "age": 25, "city": "Chennai"},
        {"name": "Ravi", "age": None, "city": "Pune"},
        {"name": "Priya", "age": 30, "city": "Chennai"},
    ]
}


def check_data_quality(dataset_id):
    if dataset_id not in DATASETS:
        return {"error": "Dataset not found"}

    rows = DATASETS[dataset_id]

    if not rows:
        return {
            "dataset_id": dataset_id,
            "status": "failed",
            "rows_checked": 0,
            "warnings": ["Dataset is empty"]
        }

    warnings = []
    columns = set()

    for row in rows:
        columns.update(row.keys())

    for column in sorted(columns):
        missing = sum(
            1 for row in rows
            if row.get(column) is None or row.get(column) == ""
        )

        percentage = missing / len(rows) * 100

        if percentage > 0:
            recommendation = None

            if percentage >= 30:
                recommendation = {
                    "action": "IMPUTE_OR_DROP",
                    "text": "Impute missing values or drop the column.",
                    "params": {
                        "suggested_strategy": (
                            "median" if column == "age"
                            else "most_frequent"
                        )
                    }
                }

            warnings.append({
                "code": (
                    "HIGH_NULL_RATIO"
                    if percentage >= 30
                    else "NULL_VALUES_FOUND"
                ),
                "severity": "warning",
                "column": column,
                "message": f"{percentage:.0f}% of values are missing.",
                "recommendation": recommendation
            })

    for row in rows:
        age = row.get("age")
        if isinstance(age, (int, float)) and age < 0:
            warnings.append({
                "code": "INVALID_AGE",
                "severity": "error",
                "column": "age",
                "message": "Negative age value found.",
                "recommendation": {
                    "action": "VALIDATE_RANGE",
                    "text": "Correct negative age values.",
                    "params": {"minimum": 0}
                }
            })
            break

    if any(w["severity"] == "error" for w in warnings):
        status = "failed"
    elif warnings:
        status = "warning"
    else:
        status = "success"

    return {
        "dataset_id": dataset_id,
        "status": status,
        "rows_checked": len(rows),
        "warnings": warnings
    }


result = check_data_quality("dataset001")
print(result)
