import pandas as pd
from fpdf import FPDF
import os

def generate_report():

    csv_path = "data/location_log.csv"

    if not os.path.exists(csv_path):
        print("CSV file not found!")
        return

    df = pd.read_csv(csv_path)

    total_records = len(df)

    theft_count = len(
        df[df["Status"] == "THEFT SUSPECTED"]
    )

    safe_count = len(
        df[df["Status"] == "MOVING SAFELY"]
    )

    parked_count = len(
        df[df["Status"] == "PARKED"]
    )

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Vehicle Tracking Report", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)

    pdf.set_font("Helvetica", "", 12)

    pdf.cell(0, 8, f"Total Records: {total_records}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Safe Movements: {safe_count}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Parked Records: {parked_count}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Theft Alerts: {theft_count}", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(8)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Recent Vehicle Logs", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(2)

    pdf.set_font("Helvetica", "", 9)

    recent_logs = df.tail(10)

    for _, row in recent_logs.iterrows():

        log_text = (
            f"Time: {row['Timestamp']} | "
            f"Lat: {row['Latitude']} | "
            f"Lon: {row['Longitude']} | "
            f"Status: {row['Status']}"
        )

        pdf.multi_cell(
            180,
            6,
            log_text
        )

    os.makedirs("reports", exist_ok=True)

    output_path = "reports/Vehicle_Report.pdf"

    pdf.output(output_path)

    print(f"\nReport Generated Successfully!")
    print(f"Saved at: {output_path}")

if __name__ == "__main__":
    generate_report()