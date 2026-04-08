import sys
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QFileDialog, QVBoxLayout, QMessageBox
)


class ModelRunner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenModelica Runner")

        layout = QVBoxLayout()

        # File input
        self.file_label = QLabel("Select Executable:")
        self.file_input = QLineEdit()
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.browse_file)

        # Start time
        self.start_label = QLabel("Start Time:")
        self.start_input = QLineEdit()

        # Stop time
        self.stop_label = QLabel("Stop Time:")
        self.stop_input = QLineEdit()

        # Run button
        self.run_btn = QPushButton("Run Simulation")
        self.run_btn.clicked.connect(self.run_model)

        layout.addWidget(self.file_label)
        layout.addWidget(self.file_input)
        layout.addWidget(self.browse_btn)
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_input)
        layout.addWidget(self.stop_label)
        layout.addWidget(self.stop_input)
        layout.addWidget(self.run_btn)

        self.setLayout(layout)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self)
        self.file_input.setText(file_path)

    def run_model(self):
        exe = self.file_input.text()
        start = self.start_input.text()
        stop = self.stop_input.text()

        try:
            start = int(start)
            stop = int(stop)

            if not (0 <= start < stop < 5):
                raise ValueError
        except:
            QMessageBox.warning(self, "Error", "Enter valid values (0 <= start < stop < 5)")
            return

        try:
            cmd = [exe, f"-override=startTime={start},stopTime={stop}"]
            subprocess.run(cmd)
            QMessageBox.information(self, "Done", "Simulation executed!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelRunner()
    window.show()
    sys.exit(app.exec())