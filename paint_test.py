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

    def __draw_back(self):
        """初始化背景为黑色"""
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#000000'))
        self.setPalette(palette)

    def __draw_block(self):
        """画背景方框"""
        margin_left, margin_right, margin_top, margin_bottom = 80, 80, 20, 20

        painter = QPainter(self)
        pen = QPen()
        pen.setColor(QColor('#FF0000'))
        painter.setPen(pen)

        # 左右两根垂直线
        painter.drawLine(margin_left, self.height() - margin_top,
                         margin_left, margin_bottom)
        painter.drawLine(self.width() - margin_right, self.height() - margin_top,
                         self.width() - margin_right, margin_bottom)

        # 水平线
        cell_grid_height = 60
        xleft = margin_left
        xright = self.width() - margin_right

        ybegin = margin_bottom
        yend = self.height() - margin_top

        grid_height = yend - ybegin
        cells = grid_height // cell_grid_height
        each_grid_height = grid_height / cells

        ypoints = [margin_bottom + i * each_grid_height for i in range(cells + 1)]
        for idx, ypoint in enumerate(ypoints):
            if idx == 0 or idx == len(ypoints) - 1:
                pen.setStyle(Qt.SolidLine)
            else:
                pen.setStyle(Qt.DashDotLine)
            painter.setPen(pen)
            painter.drawLine(xleft, ypoint, xright, ypoint)


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
