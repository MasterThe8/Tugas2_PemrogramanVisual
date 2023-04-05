import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWork(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tugas 2")
        self.setGeometry(500,300, 500,400)
        self.resize(400,200)
        
        layout = QVBoxLayout()
        self.sp = QSpinBox()
        self.nim = QLabel("F1D0XXXXX")
        self.out = QLineEdit
        
        self.nim.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.nim)
        layout.addWidget(self.sp)
        
        self.sp.valueChanged.connect(self._on_change)
        
        self.setLayout(layout)
        self.setWindowTitle("SpinBox demo")
            
    def _on_change(self):  
        current = self.sp.value()
        self.nim.setText("F1D0" + str(current))
        self.sp.setMinimum(21090)
        self.sp.setMinimum(21099)
       

app = QApplication(sys.argv)
window = MyWork()
window.show()
sys.exit(app.exec())