import sys
import signal
import traceback

from collections import namedtuple

from PyQt5.QtCore import Qt, QPoint, QLine, QTimer

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, \
    QSplitter, QMessageBox
from PyQt5.QtGui import QPainter, QPalette, QColor, QPen

from hq_data import Kline
from hq_data import HqData
from exception import hook_exception_handle


class PaintArea(QWidget):
    """
    背景基类,画垂直两根线以及水平分割线
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__draw_back()
        self.__set_default()
        self.__calc_grid()

    def paintEvent(self, QPaintEvent):
        self.__draw_block()

    def resizeEvent(self, QResizeEvent):
        self.__calc_grid()

    def __set_default(self):
        """
        设置:
        边距               self.margin
        单个grid的最小高度  self.min_grid_height
        """

        # 边距
        Margin = namedtuple('Margin', 'left right top bottom')
        self.margin = Margin(left=80, right=80, top=20, bottom=20)

        # 单个grid的最小高度
        self.min_grid_height = 60

    def __calc_grid(self):
        """
        计算:
        画板的长度和宽度    self.grid
        4点确定矩形         self.rectangle
        分割成grid的个数    self.min_grids
        每个grid的高度      self.each_grid_height
        横线y轴坐标集合     self.y_coordinates
        """

        # 画板的长度和宽度
        Grid = namedtuple('Grid', 'height width')
        self.grid = Grid(self.height() - self.margin.top - self.margin.bottom,
                         self.width() - self.margin.left - self.margin.right)

        # 4点确定矩形
        Rectangle = namedtuple('Rectangle', 'x1 x2 y1 y2')
        self.rectangle = Rectangle(x1=self.margin.left,
                                   x2=self.width() - self.margin.right,
                                   y1=self.margin.bottom,
                                   y2=self.height() - self.margin.top)

        # 分割成grid的个数
        self.min_grids = self.grid.height // self.min_grid_height
        # 每个grid的高度
        self.each_grid_height = self.grid.height / self.min_grids
        # 横线y轴坐标集合
        self.y_coordinates = [self.margin.bottom + i * self.each_grid_height
                              for i in range(self.min_grids + 1)]

    def __draw_back(self):
        """初始化背景为黑色"""
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#000000'))
        self.setPalette(palette)

    def __draw_block(self):
        """画左右两根垂直线,横线列表"""
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(QColor('#FF0000'))
        painter.setPen(pen)

        # 左右两根垂直线
        painter.drawLine(self.rectangle.x1, self.rectangle.y1,
                         self.rectangle.x1, self.rectangle.y2)

        painter.drawLine(self.rectangle.x2, self.rectangle.y1,
                         self.rectangle.x2, self.rectangle.y2)

        # 横线
        for idx, y_corrdinate in enumerate(self.y_coordinates):
            if idx == 0 or idx == len(self.y_coordinates) - 1:
                pen.setStyle(Qt.SolidLine)
            else:
                pen.setStyle(Qt.DashDotLine)
            painter.setPen(pen)
            painter.drawLine(self.rectangle.x1, y_corrdinate,
                             self.rectangle.x2, y_corrdinate)


class KlineArea(PaintArea):
    def __init__(self):
        # 读行情,测试用
        super().__init__()
        self.hqdata = HqData('./dataKLine.txt')
        self.hqdata.load_hq()
        self.__set_default()

    def __set_default(self):
        """
        设置:
        总显示数量    self.total
        日期间隔      self.day_section
        最高价,最低价 self.price
        """

        # 总显示数量
        self.total = 200

        # 日期间隔
        DaySection = namedtuple('DaySection', 'begin end')

        self.day_section = DaySection(begin=len(self.hqdata.klines) - self.total,
                                      end=len(self.hqdata.klines))

        # 最高价,最低价
        Price = namedtuple('Price', 'highest_bid lowest_bid')

        highest_bid = self.hqdata.klines[0].highest_bid
        lowest_bid = self.hqdata.klines[0].lowest_bid

        for i in range(self.day_section.begin, self.day_section.end):
            if self.hqdata.klines[i].highest_bid > highest_bid:
                highest_bid = self.hqdata.klines[i].highest_bid
            if self.hqdata.klines[i].lowest_bid < lowest_bid:
                lowest_bid = self.hqdata.klines[i].lowest_bid

        self.price = Price(highest_bid, lowest_bid)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('paint test')
        self.resize(1000, 600)
        splitter = QSplitter(Qt.Vertical)
        paint_area1 = KlineArea()
        paint_area2 = PaintArea()
        splitter.addWidget(paint_area1)
        splitter.addWidget(paint_area2)
        splitter.setHandleWidth(1)
        self.setCentralWidget(splitter)


if __name__ == '__main__':
    hook_exception_handle()

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
