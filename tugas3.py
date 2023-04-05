import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tugas 3')
        self.setGeometry(500,300, 500,400)
        self.resize(400,100)

        layout = QFormLayout()
        self.setLayout(layout)

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(0, 9)
        slider.setValue(21090)
        slider.setMaximum(21099)
        slider.setMinimum(21090)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        slider.valueChanged.connect(self.update)

        self.result_label = QLabel('NIM : F1D0XXXXX', self)
        self.result_label.setFont(QFont("Calibri", 24))

        layout.addRow(slider)
        layout.addRow(self.result_label)

        self.show()

    def update(self, value):
        self.result_label.setText(f'NIM : F1D0{value}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())