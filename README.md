# OpenModelica-Desktop-App
Desktop GUI application using PyQt6 to run OpenModelica simulation executables

# OpenModelica Desktop App (FOSSEE Screening Task 2026)

## 📌 Project Overview
This project is a desktop GUI application built using **Python (PyQt6)** that allows users to execute an OpenModelica compiled simulation model through a simple interface.

The application enables:
- Selecting an executable file generated from OpenModelica
- Providing simulation parameters (start and stop time)
- Running the simulation directly from the GUI

---

## 🚀 Features
- Browse and select executable file
- Input fields for start time and stop time
- Run simulation with a single click
- Clean and user-friendly interface

---

## ⚙️ Technologies Used
- Python 3.10+
- PyQt6
- OpenModelica

---

## 🧪 Model Used
- Model Name: **TwoConnectedTanks**
- Compiled using OpenModelica (OMEdit)

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install PyQt6

2. Run the application
python app.py

🖥️ Usage Instructions:
Click Browse
Select the executable file (TwoConnectedTanks.exe) from the downloaded model folder
Enter:
Start Time: 0
Stop Time: 2
Click Run Simulation

📂 Model Files
Due to large file size, the OpenModelica executable and all dependent files are hosted on Google Drive.

👉 Download here:
https://drive.google.com/drive/folders/1oGJwAfEmCPM4EsZz-6c4L6-hekoNV2Hk?usp=drive_link

Steps:
Open the above link
Download the folder
Extract if required
Select TwoConnectedTanks.exe inside the application

⚠️ Notes
The simulation may show warnings (e.g., division by zero), but execution is successful.
The objective of this task is GUI-based execution, not model correctness.

📸 Output Screenshot
![Simulation Output](output/final_output.png)

🧠 Design Approach
Focused on minimal and intuitive UI
Ensured easy file selection and execution flow
Maintained compatibility with OpenModelica runtime dependencies

✨ Author
Priyavarshini V
