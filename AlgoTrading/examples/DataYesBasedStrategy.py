# -*- coding: utf-8 -*-
u"""
Created on 2015-7-31

@author: cheng.li
"""

import datetime as dt

from AlgoTrading.Strategy.Strategy import Strategy
from AlgoTrading.Backtest.Backtest import Backtest
from AlgoTrading.Data.DataProviders import DataYesMarketDataHandler
from AlgoTrading.Execution.Execution import SimulatedExecutionHandler
from AlgoTrading.Portfolio.Portfolio import Portfolio
from PyFin.Analysis.TechnicalAnalysis import SecurityMovingAverage as MA


class MovingAverageCrossStrategy(Strategy):

    def __init__(self,
                 bars,
                 events,
                 symbolList,
                 shortWindow=10,
                 longWindow=30):
        self.bars = bars
        self.symbolList = self.bars.symbolList
        self.events = events
        self.short_sma = MA(shortWindow, 'close', symbolList)
        self.long_sma = MA(longWindow, 'close', symbolList)
        self.bought = self._calculateInitialBought()

    def calculateSignals(self, event):
        short_sma = self.short_sma.value
        long_sma = self.long_sma.value
        for s in self.symbolList:
            symbol = s
            currDt = self.bars.getLatestBarDatetime(s)
            if short_sma[s] > long_sma[s] and self.bought[s] == 'OUT':
                print("{0}: BUY {1}".format(currDt, s))
                sigDir = 'LONG'
                self.order(symbol, sigDir)
                self.bought[s] = 'LONG'
            if short_sma[s] < long_sma[s] and self.bought[s] == "LONG":
                print("{0}: SELL {1}".format(currDt, s))
                sigDir = 'EXIT'
                self.order(symbol, sigDir)
                self.bought[s] = 'OUT'

    def _calculateInitialBought(self):
        self._subscribe()
        bought = {}
        for s in self.symbolList:
            bought[s] = 'OUT'
        return bought


def run_example():
    symbolList = ['600000.xshg', '000001.xshe']
    initialCapital = 100000.0
    heartbeat = 0.0
    startDate = dt.datetime(2010, 1, 2)
    endDate = dt.datetime(2015, 9, 15)

    dataHandler = DataYesMarketDataHandler(token="2bfc4b3b06efa5d8bba2ab9ef83b5d61f1c3887834de729b60eec9f13e1d4df8",
                                           symbolList=symbolList,
                                           startDate=startDate,
                                           endDate=endDate)

    backtest = Backtest(symbolList,
                        initialCapital,
                        heartbeat,
                        dataHandler,
                        SimulatedExecutionHandler,
                        Portfolio,
                        MovingAverageCrossStrategy)

    backtest.simulateTrading()

if __name__ == "__main__":
    run_example()
