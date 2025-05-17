import sys
import random
from PyQt6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["你好世界", "Hello World", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("点击我!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec()) 