import fitz  # PyMuPDF

def embed_js(pdf_filename, js_filename):
    doc = fitz.open(pdf_filename)
    
    # Read JavaScript from file
    with open(js_filename, "r") as f:
        js_code = f.read()
    
    # Embed JavaScript at the document level (NOT page level)
    doc.set_js(js_code)
    
    # Save the updated PDF
    output_pdf = "tetrispdf_with_js.pdf"
    doc.save(output_pdf)
    print(f"✅ JavaScript embedded successfully! Check '{output_pdf}'.")

if __name__ == "__main__":
    embed_js("tetrispdf_grid.pdf", "tetris.js")
