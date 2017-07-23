import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, \
    QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QGridLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('kline_test')
        self.resize(300, 300)

        widget = QWidget()

        grid = QGridLayout()

        grid.addWidget(self.get_buttons_box(), 0, 0)
        grid.addWidget(self.get_buttons2_box(), 0, 1)
        grid.addWidget(QPushButton('&退出'),1,1)
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    def get_buttons_box(self):
        groupbox = QGroupBox()

        box = QVBoxLayout()
        box.addWidget(QPushButton('&1'))
        box.addWidget(QPushButton('&2'))
        box.addWidget(QPushButton('&3'))
        box.addWidget(QPushButton('&4'))
        box.addWidget(QPushButton('&5'))
        box.addStretch(1)

        groupbox.setLayout(box)

        return groupbox

    def get_buttons2_box(self):
        groupbox = QGroupBox()

        box = QVBoxLayout()
        box.addWidget(QPushButton('&一'))
        box.addWidget(QPushButton('&二'))
        box.addWidget(QPushButton('&三'))
        box.addWidget(QPushButton('&四'))
        box.addWidget(QPushButton('&五'))
        box.addStretch(1)
        groupbox.setLayout(box)

        return groupbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
