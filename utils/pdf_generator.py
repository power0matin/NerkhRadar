from datetime import datetime
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Weekly Market Report", 0, 1, "C")

def generate_weekly_report(data):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}", 0, 1)
    for key, value in data.items():
        pdf.cell(0, 10, f"{key}: {value}", 0, 1)
    pdf.output("weekly_report.pdf")