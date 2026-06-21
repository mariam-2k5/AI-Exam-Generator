from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(text):

    file_path = "exam_paper.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    y = height - 50

    lines = text.split("\n")

    for line in lines:

        # CENTER ALIGN HEADINGS
        if (
            "College" in line
            or "Examination" in line
            or "Section A" in line
            or "Section B" in line
            or "Section C" in line
        ):
            c.setFont("Helvetica-Bold", 12)
            c.drawCentredString(width / 2, y, line)

        else:
            c.setFont("Helvetica", 11)
            c.drawString(50, y, line)

        y -= 18

        if y < 50:
            c.showPage()
            y = height - 50

    c.save()

    return file_path