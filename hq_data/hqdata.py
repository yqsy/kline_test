from copy import copy
class Kline():
    def __init__(self):
        self.time = ''  # 时间
        self.open_price = 0.0  # 开盘
        self.highest_bid = 0.0  # 最高
        self.lowest_bid = 0.0  # 最低
        self.closing_price = 0.0  # 收盘
        self.amount_of_increase = 0.0  # 涨幅
        self.amount_of_amplitude = 0.0  # 振幅
        self.total_volume = ''  # 总手
        self.total_amount = ''  # 金额
        self.turnover_rate = 0.0  # 换手率
        self.volume_amount = 0.0  # 成交次数
        self.average_line5 = 0.0  # 5日均线
        self.average_line10 = 0.0  # 10日均线
        self.average_line20 = 0.0  # 20日均线
        self.average_line30 = 0.0  # 30日均线
        self.average_line60 = 0.0  # 60日均线
        self.ftotal_volume = 0.0  # 总成交量
        self.ftotal_amount = 0.0  # 总金额
        self.volume_average5 = 0.0  # 成交量5日均值
        self.volume_average10 = 0.0  # 成交量10日均值


class HqData():
    def __init__(self, file):
        self.file = file
        self.klines = []

    def load_hq(self):
        with open(self.file, 'r', encoding='gb2312') as f:
            kline = Kline()
            for line in f:
                eles = line.split('\t')

                if len(eles) < 11:
                    continue

                kline.time = eles[0]
                kline.open_price = float(eles[1])
                kline.highest_bid = float(eles[2])
                kline.lowest_bid = float(eles[3])
                kline.closing_price = float(eles[4])
                kline.amount_of_increase = float(eles[5].rstrip('%'))
                kline.amount_of_amplitude = float(eles[6].rstrip('%'))
                kline.total_volume = eles[7]
                kline.total_amount = eles[8]
                kline.turnover_rate = eles[9]
                kline.volume_amount = float(eles[10].replace('-','0'))

                self.klines.append(copy(kline))