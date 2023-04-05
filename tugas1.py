import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class MyWork(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tugas 1")
        self.setGeometry(500,300, 500,400)
        self.resize(400,100)

        vbox = QVBoxLayout()
        self.combo = QComboBox()

        self.combo.addItem("NIM")
        self.combo.addItem("F1D019092")
        self.combo.addItem("F1D020092")
        self.combo.addItem("F1D021092")
        self.combo.addItem("F1D022092")

        self.combo.currentIndexChanged.connect(self._on_select)
        self.label = QLabel("")
        self.label.setFont(QFont("Calibri", 24))

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def _on_select(self):
        item = self.combo.currentText()
        self.label.setText("NIM Saya : " + item)


app = QApplication(sys.argv)
window = MyWork()
window.show()
sys.exit(app.exec())