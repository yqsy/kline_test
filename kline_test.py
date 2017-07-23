import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('kline_test')
        self.resize(870, 550)

        # 默认水平分割
        splitter_main = QSplitter()
        splitter_vertical1 = QSplitter(splitter_main)
        splitter_vertical2= QSplitter(splitter_main)
        self.setCentralWidget(splitter_main)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
