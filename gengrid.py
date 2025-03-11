from reportlab.pdfgen import canvas

GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 20

def create_pdf_grid(output_pdf):
    c = canvas.Canvas(output_pdf)
    c.setPageSize((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))

    # Draw the grid & create form fields
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            field_name = f"P_{x}_{y}"
            c.rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE, stroke=1, fill=0)
            c.acroForm.textfield(name=field_name, x=x * CELL_SIZE, y=y * CELL_SIZE, width=CELL_SIZE, height=CELL_SIZE)

    c.save()

create_pdf_grid("tetrispdf_grid.pdf")