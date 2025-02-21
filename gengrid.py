from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 20  # size of each block in points
MARGIN = 50

def draw_grid(c):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            x_pos = MARGIN + x * CELL_SIZE
            y_pos = MARGIN + y * CELL_SIZE
            c.rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            field_name = f"P_{x}_{y}"
            c.acroForm.textfield(
                name=field_name,
                tooltip=f"Block ({x},{y})",
                x=x_pos, y=y_pos,
                width=CELL_SIZE, height=CELL_SIZE,
                borderWidth=0,
                fillColor=None,
                textColor=None,
                forceBorder=False
            )

def generate_pdf(filename="tetrispdf_grid.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    draw_grid(c)
    c.save()
    print(f"✅ PDF generated: {filename}")

if __name__ == "__main__":
    generate_pdf()
