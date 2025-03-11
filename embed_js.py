from PyPDF2 import PdfReader, PdfWriter

def embed_js(input_pdf, output_pdf, js_code):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_js(js_code)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# Read JavaScript code from tetris.js
with open("tetris.js", "r") as js_file:
    js_code = js_file.read()

# Embed JavaScript into the PDF
embed_js("tetrispdf_grid.pdf", "tetrispdf_with_js.pdf", js_code)
print("✅ JavaScript embedded successfully! Check 'tetrispdf_with_js.pdf'.")