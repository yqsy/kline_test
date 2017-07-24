import sys

from collections import namedtuple

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QGroupBox, QLabel, \
    QLineEdit, QBoxLayout, QTableView, QFormLayout, QVBoxLayout, QTreeView

from PyQt5.QtGui import QStandardItemModel


class MyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(120)


pihao, zcmc, mm, wtsl, wtj, cjsl, cjj, jyzh, zqdm, jysc = range(10)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('快枪手 v1.0.0')
        self.resize(800, 400)

        widget = QWidget()
        grid_layout = QGridLayout()

        widget.setLayout(grid_layout)
        grid_layout.addWidget(self.get_box_buy(), 0, 0)
        grid_layout.addWidget(self.get_box_sell(), 1, 0)
        grid_layout.addWidget(self.get_gox_chedanweituo(), 0, 1)
        grid_layout.addWidget(self.get_box_chengjiaoxinxi(), 1, 1)

        grid_layout.setColumnStretch(0,1)
        grid_layout.setColumnStretch(1,3)

        #setRowStretch
        self.setCentralWidget(widget)

    def get_box_buy(self):
        """左上角的买入方框"""
        box = QGroupBox('买入')
        form_layout = QFormLayout()
        form_layout.addRow('证券代码:', MyLineEdit('000001'))
        form_layout.addRow('证券名称:', MyLineEdit('平安银行'))
        form_layout.addRow('委托价格:', MyLineEdit('16.300'))
        form_layout.addRow('委托数量:', MyLineEdit('700'))
        form_layout.addRow('可买数量:', MyLineEdit('700'))
        box.setLayout(form_layout)
        return box

    def get_box_sell(self):
        """左下角的卖出方框"""
        box = QGroupBox('卖出')
        form_layout = QFormLayout()
        form_layout.addRow('证券代码:', MyLineEdit('000001'))
        form_layout.addRow('证券名称:', MyLineEdit('平安银行'))
        form_layout.addRow('委托价格:', MyLineEdit(''))
        form_layout.addRow('委托数量:', MyLineEdit(''))
        form_layout.addRow('可买数量:', MyLineEdit(''))
        box.setLayout(form_layout)
        return box

    def get_gox_chedanweituo(self):
        """右上角的撤单委托方框"""
        box = QGroupBox('撤单委托')
        layout = QVBoxLayout()
        tree_view = QTreeView()
        layout.addWidget(tree_view)
        tree_view.setModel(self.create_model(self))
        box.setLayout(layout)
        return box

    def get_box_chengjiaoxinxi(self):
        """右下角的成交信息"""
        box = QGroupBox('成交信息')
        layout = QVBoxLayout()
        tree_view = QTreeView()
        layout.addWidget(tree_view)
        tree_view.setModel(self.create_model(self))
        box.setLayout(layout)
        return box

    @staticmethod
    def add_row(model, named_tuple):
        model.insertRow(0)
        model.setData(model.index(0, pihao), named_tuple.pihao)
        model.setData(model.index(0, zcmc), named_tuple.zcmc)
        model.setData(model.index(0, mm), named_tuple.mm)
        model.setData(model.index(0, wtsl), named_tuple.wtsl)
        model.setData(model.index(0, wtj), named_tuple.wtj)
        model.setData(model.index(0, cjsl), named_tuple.cjsl)
        model.setData(model.index(0, cjj), named_tuple.cjj)
        model.setData(model.index(0, jyzh), named_tuple.jyzh)
        model.setData(model.index(0, zqdm), named_tuple.zqdm)
        model.setData(model.index(0, jysc), named_tuple.jysc)

    @staticmethod
    def create_model(parent):
        model = QStandardItemModel(0, 10, parent)
        model.setHeaderData(pihao, Qt.Horizontal, '批号-比数')
        model.setHeaderData(zcmc, Qt.Horizontal, '证券名称')
        model.setHeaderData(mm, Qt.Horizontal, '买卖')
        model.setHeaderData(wtsl, Qt.Horizontal, '委托数量')
        model.setHeaderData(wtj, Qt.Horizontal, '委托价')
        model.setHeaderData(cjsl, Qt.Horizontal, '成交数量')
        model.setHeaderData(cjj, Qt.Horizontal, '成交价')
        model.setHeaderData(jyzh, Qt.Horizontal, '交易账号')
        model.setHeaderData(zqdm, Qt.Horizontal, '证券代码')
        model.setHeaderData(jysc, Qt.Horizontal, '交易市场')

        CDWT = namedtuple('CDWT', 'pihao zcmc mm wtsl wtj cjsl cjj jyzh zqdm jysc')

        MainWindow.add_row(model, CDWT(pihao='13-1', zcmc='方正科技', mm='买', wtsl='100',
                                       wtj='10.650', cjsl='0', cjj='0.000', jyzh='A122134141',
                                       zqdm='600601', jysc='沪A[1]'))

        MainWindow.add_row(model, CDWT(pihao='5-1', zcmc='方正科技', mm='买', wtsl='100',
                                       wtj='10.650', cjsl='0', cjj='0.000', jyzh='A122134141',
                                       zqdm='600601', jysc='沪A[1]'))

        MainWindow.add_row(model, CDWT(pihao='1-1', zcmc='登记指定', mm='指', wtsl='1',
                                       wtj='1.000', cjsl='0', cjj='0.000', jyzh='A122134141',
                                       zqdm='799999', jysc='沪A[1]'))

        return model


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
