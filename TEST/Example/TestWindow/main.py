import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 设置应用程序样式
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 