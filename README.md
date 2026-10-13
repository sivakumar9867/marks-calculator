# MARKS / LAB — Result Studio

A Flask-based marks calculator with a custom-designed, responsive interface. The interface uses a dark editorial style, acid-lime accents, orbital artwork drawn in CSS, live score previews, and a clear subject breakdown.

## Features

- Student name and marks for Python, C Programming, and Data Structures & Algorithms.
- Live total and average preview as marks are entered.
- Subject-level result indicators and overall result report.
- **Original pass rule preserved:** a student passes only when every subject score is at least 35/100.
- Input validation for empty values, non-integer marks, and marks outside 0–100.
- Responsive desktop/mobile layout and print-friendly result report.
- No account or database; entered student information is not saved by the app.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

## Project structure

```text
marks-calculator/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── app.js
│   └── style.css
├── .gitignore
└── README.md
```

## Calculation rules

- Maximum marks: 100 per subject (300 total).
- Pass threshold: 35 marks in **each** subject.
- Total = Python + C Programming + DSA.
- Overall percentage = total / 300 × 100.
- If any subject is below 35, the overall status is **NEEDS ATTENTION** (fail under the original rule).

## Built with

Python · Flask · HTML · CSS · JavaScript

## Note

This is an educational project. The report reflects only the values entered into the form; it is not an official academic marksheet.
