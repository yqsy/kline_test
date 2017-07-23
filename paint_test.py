import sys

from PyQt5.QtCore import Qt, QPoint

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, \
    QSplitter
from PyQt5.QtGui import QPainter, QPalette, QColor, QPen


class PaintArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draw_back()

    def paintEvent(self, QPaintEvent):
        self.draw_block()

    def draw_back(self):
        """初始化背景为黑色"""
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#000000'))
        self.setPalette(palette)

    def draw_horizontal_line(self):
        """画背景横线"""
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(QColor('#FF0000'))
        painter.setPen(pen)

    def draw_block(self):
        """画背景方框"""

        margin_left = 80
        margin_right = 80
        margin_top = 20
        margin_bottom = 20

        painter = QPainter(self)
        pen = QPen()
        pen.setColor(QColor('#FF0000'))
        painter.setPen(pen)

        # 4个角的坐标 左上 左下 右上 右下
        points = [
            QPoint(margin_left, self.height() - margin_top),
            QPoint(margin_left, margin_bottom),
            QPoint(self.width() - margin_right, self.height() - margin_top),
            QPoint(self.width() - margin_right, margin_bottom)
        ]

        upper_left, lower_left, upper_right, lower_right = range(4)

        painter.drawLine(points[upper_left], points[lower_left])
        painter.drawLine(points[upper_left], points[upper_right])

        painter.drawLine(points[lower_right], points[lower_left])
        painter.drawLine(points[lower_right], points[upper_right])


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('paint test')
        self.resize(1000, 600)
        splitter = QSplitter(Qt.Vertical)
        paint_area1 = PaintArea()
        paint_area2 = PaintArea()
        splitter.addWidget(paint_area1)
        splitter.addWidget(paint_area2)
        splitter.setHandleWidth(1)
        self.setCentralWidget(splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
