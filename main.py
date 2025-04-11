import backtrader as bt
import yfinance as yf
import datetime

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1 = bt.ind.SMA(period=10)
        sma2 = bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(SmaCross)

    data = bt.feeds.PandasData(
        dataname=yf.download('AAPL', '2022-01-01', '2023-01-01')
    )
    cerebro.adddata(data)
    cerebro.run()
    cerebro.plot()
