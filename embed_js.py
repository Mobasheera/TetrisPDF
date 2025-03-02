import pikepdf

# Load the existing PDF
pdf = pikepdf.Pdf.open("tetrispdf_grid.pdf")

# Read the JavaScript code from tetris.js
with open("tetris.js", "r") as js_file:
    js_code = js_file.read()

# Embed the JavaScript into the PDF
pdf.Root.AA = pikepdf.Dictionary()
pdf.Root.AA.O = pikepdf.Dictionary(JS=pikepdf.String(js_code))

# Save the new PDF with JavaScript embedded
pdf.save("tetrispdf_with_js.pdf")
print("✅ JavaScript embedded successfully! Check 'tetrispdf_with_js.pdf'.")