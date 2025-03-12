import fitz  # PyMuPDF

def create_pdf(output_filename="tetrispdf_grid.pdf"):
    doc = fitz.open()
    page = doc.new_page()
    text = "Tetris Grid"
    page.insert_text((100, 100), text, fontsize=20)
    doc.save(output_filename)
    print(f"PDF saved as {output_filename}")

if __name__ == "__main__":
    create_pdf()