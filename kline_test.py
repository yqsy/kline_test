import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, \
    QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QGridLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('kline_test')
        self.resize(870, 550)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
