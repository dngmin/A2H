import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from core.python import A2H



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.core = A2H()

        self.setWindowTitle("A2H")

        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.layout = QVBoxLayout(self.container)

        self.input_label = QLabel("Input")
        self.input_edit = QLineEdit()
        self.convert_button = QPushButton("Convert")
        self.input_edit.returnPressed.connect(lambda :self.convert(self.input_edit.text()))
        self.convert_button.clicked.connect(lambda :self.convert(self.input_edit.text()))
        self.output_label = QLabel("Outputt")
        self.output_edit = QLineEdit()

        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_edit)
        self.layout.addWidget(self.convert_button)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_edit)

    def convert(self, input_string):
        converted = self.core.run(input_string)
        self.output_edit.setText(converted)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())