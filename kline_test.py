import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, \
    QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, \
    QGridLayout, QWidget, QBoxLayout, QLabel, QLineEdit, QCheckBox, \
    QTreeWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('kline_test')
        self.resize(300, 300)

        widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_left_box(), 0, 0)
        grid_layout.addWidget(self.get_right_box(), 0, 1)
        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)

    def get_left_box(self):
        box = QGroupBox('left')

        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel('label1'), 0, 0)
        grid_layout.addWidget(QLineEdit(''), 0, 1)
        grid_layout.addWidget(QLabel('label2'), 1, 0)
        grid_layout.addWidget(QLineEdit(''), 1, 1)
        grid_layout.addWidget(QCheckBox('check box'), 2, 0, 1, 2)
        grid_layout.addWidget(QTreeWidget(), 3, 0, 1, 2)
        grid_layout.addWidget(QLabel('label4'), 4, 0, 1, 2)

        box.setLayout(grid_layout)
        return box

    def get_right_box(self):
        box = QGroupBox('right')

        qbox_layout = QVBoxLayout()
        qbox_layout.addWidget(QPushButton('button1'))
        qbox_layout.addWidget(QPushButton('button2'))
        qbox_layout.addWidget(QPushButton('button3'))
        qbox_layout.addStretch(2)
        qbox_layout.addWidget(QPushButton('button4'))

        box.setLayout(qbox_layout)
        return box


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
