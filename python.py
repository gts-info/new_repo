"""
DataFlow Dashboard - Sample Python Script
Run: python dataflow_dashboard.py
 
This is a console-based demo using mock/sample data.
It does not connect to a real API or database.
"""
 
from datetime import datetime
 
# Clearly marked sample data (in-memory demo records)
PROJECTS = [
    {"id": "PRJ-001", "name": "Customer Churn Prediction", "status": "Active"},
    {"id": "PRJ-002", "name": "Sales Forecasting", "status": "Active"},
    {"id": "PRJ-003", "name": "Fraud Detection", "status": "Draft"},
]
 
DATASETS = [
    {"id": "DS-001", "name": "customer_data.csv", "rows": 12500, "status": "Ready"},
    {"id": "DS-002", "name": "sales_history.csv", "rows": 8400, "status": "Ready"},
    {"id": "DS-003", "name": "transactions.csv", "rows": 25000, "status": "Profiling"},
    {"id": "DS-004", "name": "customer_feedback.csv", "rows": 5100, "status": "Ready"},
]
 
EXPERIMENTS = [
    {"id": "EXP-001", "name": "Churn model baseline", "status": "Completed"},
    {"id": "EXP-002", "name": "Sales model comparison", "status": "Running"},
    {"id": "EXP-003", "name": "Fraud feature test", "status": "Pending"},
]
 
TRAINING_JOBS = [
    {"id": "JOB-001", "model": "Random Forest", "status": "Completed"},
    {"id": "JOB-002", "model": "XGBoost", "status": "Running"},
    {"id": "JOB-003", "model": "Logistic Regression", "status": "Failed"},
]
 
MODELS = [
    {"id": "MDL-001", "name": "Churn Classifier", "version": "v1", "status": "Ready"},
    {"id": "MDL-002", "name": "Sales Regressor", "version": "v2", "status": "Testing"},
]
 
 
def print_header(title):
    print("\n" + "=" * 68)
    print(f"  {title}")
    print("=" * 68)
 
 
def show_summary():
    print_header("DATAFLOW | DASHBOARD")
    print("Monitor datasets, experiments, model training and platform activity.")
    print("\nDEMO DASHBOARD — all records below are sample/mock data.")
    print(f"Last refreshed: {datetime.now().strftime('%d-%b-%Y %I:%M:%S %p')}")
    print("\nWORKSPACE OVERVIEW")
    print("-" * 68)
    print(f"{'Projects':<20}: {len(PROJECTS):>3}")
    print(f"{'Datasets':<20}: {len(DATASETS):>3}")
    print(f"{'Experiments':<20}: {len(EXPERIMENTS):>3}")
    print(f"{'Training jobs':<20}: {len(TRAINING_JOBS):>3}")
    print(f"{'Models':<20}: {len(MODELS):>3}")
 
 
def show_records(title, records, fields):
    print_header(title)
    if not records:
        print("No records found.")
        return
 
    headings = [label for label, _ in fields]
    widths = [max(len(label), 14) for label in headings]
 
    print(" | ".join(label.ljust(width) for label, width in zip(headings, widths)))
    print("-+-".join("-" * width for width in widths))
 
    for record in records:
        values = [str(record.get(key, "")) for _, key in fields]
        print(" | ".join(value[:width].ljust(width)
                         for value, width in zip(values, widths)))
 
 
def main():
    while True:
        show_summary()
        print("\nMENU")
        print("1. View projects")
        print("2. Browse datasets")
        print("3. View experiments")
        print("4. View training jobs")
        print("5. View models")
        print("0. Exit")
 
        choice = input("\nEnter your choice (0-5): ").strip()
 
        if choice == "1":
            show_records("PROJECTS", PROJECTS, [
                ("Project ID", "id"), ("Project Name", "name"), ("Status", "status")
            ])
        elif choice == "2":
            show_records("DATASETS", DATASETS, [
                ("Dataset ID", "id"), ("Dataset Name", "name"),
                ("Rows", "rows"), ("Status", "status")
            ])
        elif choice == "3":
            show_records("EXPERIMENTS", EXPERIMENTS, [
                ("Experiment ID", "id"), ("Experiment Name", "name"),
                ("Status", "status")
            ])
        elif choice == "4":
            show_records("TRAINING JOBS", TRAINING_JOBS, [
                ("Job ID", "id"), ("Model Type", "model"), ("Status", "status")
            ])
        elif choice == "5":
            show_records("MODELS", MODELS, [
                ("Model ID", "id"), ("Model Name", "name"),
                ("Version", "version"), ("Status", "status")
            ])
        elif choice == "0":
            print("\nThank you for using the DataFlow demo dashboard.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 0 to 5.")
 
        input("\nPress Enter to return to the dashboard...")
 
 
if __name__ == "__main__":
    main()