# attendance_to_excel.py
from datetime import datetime
from pathlib import Path

import pandas as pd
import os

ATTENDANCE_FILE = "attendance.csv"
current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date in YYYY-MM-DD format
EXCEL_FILE = Path(os.path.expanduser("~")) / "Desktop" / "Attendance" / f"attendance_{current_date}.xlsx"


def convert_csv_to_excel():
    try:
        # Check if CSV exists
        if not os.path.exists(ATTENDANCE_FILE):
            print("Attendance CSV file not found.")
            return

        # Read CSV and convert to Excel
        df = pd.read_csv(ATTENDANCE_FILE)
        df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')
        print(f"Attendance Excel sheet has been created: {EXCEL_FILE}")
    except Exception as e:
        print(f"Error during conversion: {e}")
