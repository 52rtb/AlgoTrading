# -*- coding: utf-8 -*-
u"""
Created on 2015-9-21

@author: cheng.li
"""

import os
import pandas.io as io
from AlgoTrading.Data.Data import DataFrameDataHandler


class HistoricalCSVDataHandler(DataFrameDataHandler):

    def __init__(self, events, csvDir, symbolList):
        self.events = events
        self.csvDir = csvDir
        self.symbolList = symbolList
        self.symbolData = {}
        self.latestSymbolData = {}
        self.continueBacktest = True

        self._openConvertCSVFiles()

    def _openConvertCSVFiles(self):
        combIndex = None
        for s in self.symbolList:
            filePath = os.path.join(self.csvDir, "{0:s}.csv".format(s))
            self.symbolData[s] = io.parsers.read_csv(filePath,
                                                     header=0,
                                                     index_col=0,
                                                     parse_dates=True,
                                                     names=['datetime', 'open', 'high', 'low', 'close', 'volume', 'adj_close']).sort()

            if combIndex is None:
                combIndex = self.symbolData[s].index
            else:
                combIndex.union(self.symbolData[s].index)

            self.latestSymbolData[s] = []

        for s in self.symbolList:
            self.symbolData[s] = self.symbolData[s].reindex(index=combIndex, method='pad').iterrows()
