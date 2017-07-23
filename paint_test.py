import sys

from PyQt5.QtCore import Qt, QPoint, QLine

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, \
    QSplitter
from PyQt5.QtGui import QPainter, QPalette, QColor, QPen


class PaintArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__draw_back()

    def paintEvent(self, QPaintEvent):
        self.__draw_block()

    def resizeEvent(self, QResizeEvent):
        pass

    def __draw_back(self):
        """初始化背景为黑色"""
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#000000'))
        self.setPalette(palette)

    def __draw_block(self):
        """画背景方框"""
        margin_left = 80
        margin_right = 80
        margin_top = 20
        margin_bottom = 20

        painter = QPainter(self)
        pen = QPen()
        pen.setColor(QColor('#FF0000'))
        painter.setPen(pen)

        # 左右两根垂直线
        left_line = QLine(QPoint(margin_left, self.height() - margin_top),
                          QPoint(margin_left, margin_bottom))

        right_line = QLine(QPoint(self.width() - margin_right, self.height() - margin_top),
                           QPoint(self.width() - margin_right, margin_bottom))

        painter.drawLine(left_line)
        painter.drawLine(right_line)

        # 水平线
        grid_height = 60

        xleft = margin_left
        xright = self.width() - margin_right

        ybegin = margin_bottom
        yend = self.height() - margin_top

        all_horizontal_lines = range(ybegin,yend,grid_height)

        for idx,ypoint in enumerate(all_horizontal_lines):
            if idx == 0 or idx == len(all_horizontal_lines) -1 :
                pen.setStyle(Qt.SolidLine)
            else:
                pen.setStyle(Qt.DashDotLine)
            painter.setPen(pen)
            horizontal_line = QLine(QPoint(xleft,ypoint),QPoint(xright, ypoint))
            painter.drawLine(horizontal_line)


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
