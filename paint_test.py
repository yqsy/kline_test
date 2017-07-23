import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, \
    QSplitter
from PyQt5.QtGui import QPainter, QPalette, QColor


class PaintArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draw_back()

    def paintEvent(self, QPaintEvent):
        pass

    def draw_back(self):
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#000000'))
        self.setPalette(palette)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('paint test')
        self.resize(1000, 600)
        splitter = QSplitter(Qt.Vertical)
        paint_area = PaintArea(self)
        paint_area2 = PaintArea(self)
        splitter.addWidget(paint_area)
        splitter.addWidget(paint_area2)
        splitter.setHandleWidth(1)
        self.setCentralWidget(splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
