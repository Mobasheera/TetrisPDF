```markdown
# 🎮 TetrisPDF — Play Tetris Inside a PDF

**TetrisPDF** is a playable version of the classic game **Tetris**, embedded entirely inside a `.pdf` file!  
No external dependencies. No browser. Just open the file in **Adobe Acrobat Reader** and start stacking blocks! 😎

> Built with Python, PDF internals, and JavaScript.  
> Inspired by [Thomas Rinsma’s PDFTris project](https://github.com/ThomasRinsma/pdftris).

---

## 📦 Features

- 🧱 Classic Tetris gameplay inside a static `.pdf`
- 🎨 Red-colored blocks on a 10×20 grid
- 🕹️ Supports both **buttons** and **keyboard controls (W/A/S/D)**
- 🏆 Displays **current score** and **high score**
- ♻️ Fully generated via Python — customizable layout and logic
- ✨ 100% JavaScript-powered inside the PDF (Acrobat JavaScript)

---

## 🚀 How to Play

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/your-username/TetrisPDF.git
   cd TetrisPDF
   ```

2. Run the generator script:
   ```bash
   python gengrid.py
   ```

3. Open the generated file:
   ```
   TetrisPDF.pdf
   ```

   > 🛑 **IMPORTANT:** Open the file in **Adobe Acrobat Reader** (not your browser).  
   > Browser viewers may not support JavaScript or game logic.

---

## 🧠 Controls

| Action   | Key / Button |
|----------|--------------|
| Move Left  | `A` or `<` |
| Move Right | `D` or `>` |
| Rotate     | `W` or `SPIN` |
| Drop Down  | `S` or `↓` |
| Restart Game | Click `Start game` |
| Type to control | Use the input field below the grid |

---

## 📈 High Score

- Your highest score is tracked **live** inside the PDF
- Scores **reset on refresh** unless saved manually in Acrobat
- For persistence, save the PDF **after playing**

---

## 🔧 Requirements

- Python 3.x (for generating the PDF)
- Adobe Acrobat Reader (for playing the game)

---

## 🧰 Files

| File         | Description                          |
|--------------|--------------------------------------|
| `gengrid.py` | Python script that generates the game PDF |
| `TetrisPDF.pdf` | The generated interactive game |
| `README.md`  | You're reading it! 📘 |

---

## 📜 Credits

- Game logic and PDF generation based on the amazing [PDFTris by Thomas Rinsma](https://github.com/ThomasRinsma/pdftris)
- Customizations, styling, high score logic, and layout tweaks by [your name]

---

## 📄 License

MIT License — use it, modify it, share it, just give credit! ❤️

---

## 🚧 Known Limitations

- JavaScript won't work in browsers like Chrome/Firefox
- High score doesn't persist unless saved in **Acrobat**
- No sound or fancy animations (yet 😉)

---

### 🕹️ Made with 💻 + 🧠 + ❤️
```
