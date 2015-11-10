# -*- coding: utf-8 -*-
u"""
Created on 2015-9-17

@author: cheng.li
"""

from distutils.core import setup

setup(
    name='AlgoTrading',
    version='0.1.0',
    url='',
    packages=['AlgoTrading',
              'AlgoTrading.Assets',
              'AlgoTrading.Backtest',
              'AlgoTrading.Data',
              'AlgoTrading.Data.DataProviders',
              'AlgoTrading.Events',
              'AlgoTrading.Execution',
              'AlgoTrading.Finance',
              'AlgoTrading.Portfolio',
              'AlgoTrading.Strategy',
              'AlgoTrading.examples',
              'AlgoTrading.Utilities',
              'AlgoTrading.tests'],
    py_modules=['AlgoTrading.__init__'],
    license='',
    author='cheng.li',
    author_email='wegamekinglc@hotmail.com',
    description='algorithmic trading framework for multiple assets'
)
