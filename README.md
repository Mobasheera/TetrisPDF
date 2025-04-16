# 🎮 TetrisPDF — Play Tetris Inside a PDF

**TetrisPDF** is a playable version of the classic game **Tetris**, embedded entirely inside a `.pdf` file!  
No external dependencies. No browser needed. Just open the file in **Adobe Acrobat Reader** and start stacking blocks! 😎

> Built with Python, PDF internals, and JavaScript.  

---

## 📦 Features

- 🧱 Classic Tetris gameplay inside a static `.pdf`
- 🎨 Red-colored blocks on a 10×20 grid
- 🕹️ Supports both **buttons** and **keyboard controls (W/A/S/D)**
- ♻️ Fully generated via Python — customizable layout and logic
- ✨ 100% JavaScript-powered inside the PDF

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

   > 🛑 **IMPORTANT:** Open the file in **Adobe Acrobat Reader** or any **supported browser**.
   > This game was tested in Chrome's PDFium PDF Engine and Firefox's PDF.js PDF Engine

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

## 📅 Mini Project Development Timeline

| Date    | Week | Task                                 | 08/1 | 15/1 | 22/1 | 05/2 | 20/2 | 05/3 | 12/3 | 19/3 | 26/3 | 02/4 | 10/4 | 16/4 |
|---------|------|--------------------------------------|------|------|------|------|------|------|------|------|------|------|------|------|
|  08/1   | 1    | Presentation 1                       | ✅   |      |      |      |      |      |      |      |      |      |      |      |
|  15/1   | 2    | Presentation 2                       |      | ✅   |      |      |      |      |      |      |      |      |      |      |
|  22/1   | 3    | Selection of topic                   |      |      | ✅   |      |      |      |      |      |      |      |      |      |
|  05/2   | 4    | CO-PO-PSO Mapping                    |      |      |      | ✅   |      |      |      |      |      |      |      |      |
|  20/2   | 5    | Grid Generation Script               |      |      |      |      | ✅   |      |      |      |      |      |      |      |
|  05/3   | 6    | Random Block Logic Development       |      |      |      |      |      | ✅   |      |      |      |      |      |      |
|  12/3   | 7    | On-screen Controls Integration       |      |      |      |      |      |      | ✅   |      |      |      |      |      |
|  19/3   | 8    | Block Rotation (Spin) Mechanism      |      |      |      |      |      |      |      | ✅   |      |      |      |      |
|  26/3   | 9    | Mid-Term Progress Presentation       |      |      |      |      |      |      |      |      | ✅   |      |      |      |
|  02/4   | 10   | Implementation of WASD Controls      |      |      |      |      |      |      |      |      |      | ✅   |      |      |
|  10/4   | 11   | Testing and Debugging                |      |      |      |      |      |      |      |      |      |      | ✅   |      |
|  16/4   | 12   | Preparation of Project Report        |      |      |      |      |      |      |      |      |      |      |      | ✅   |

---

## 🧩 CO to Mini Project Schedule Mapping

| Project Activity                         | CO1 | CO2 | CO3 | CO4 | CO5 | CO6 | CO7 | CO8 | CO9 |
|------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Presentation 1                           | ✅  |     | ✅  |     |     |     | ✅  |     |     |
| Presentation 2                           | ✅  |     | ✅  |     |     |     | ✅  |     |     |
| Selection of topic                       | ✅  | ✅  |     |     | ✅  |     |     |     |     |
| CO-PO-PSO Mapping                        | ✅  |     |     |     | ✅  | ✅  | ✅  |     | ✅  |
| Grid Generation Script                   |     | ✅  |     | ✅  |     | ✅  |     | ✅  |     |
| Random Block Logic Development           |     | ✅  |     | ✅  |     | ✅  |     | ✅  |     |
| On-screen Controls Integration           |     | ✅  |     | ✅  |     | ✅  |     | ✅  |     |
| Block Rotation (Spin) Mechanism          |     | ✅  |     | ✅  |     | ✅  |     | ✅  |     |
| Mid-Term Progress Presentation           |     |     | ✅  | ✅  |     |     | ✅  |     | ✅  |
| WASD Controls Implementation             |     | ✅  |     | ✅  |     | ✅  |     | ✅  |     |
| Testing and Debugging                    |     | ✅  |     | ✅  | ✅  | ✅  |     |     | ✅  |
| Preparation of Project Report            |     |     | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  |


---

## 📄 License

This project is licensed under the [MIT License](https://github.com/Mobasheera/TetrisPDF/blob/main/LICENSE).

---

## 🚧 Known Limitations

- No sound or fancy animations (yet 😉)

---

### 🕹️ Made with 💻 + 🧠 + ❤️
