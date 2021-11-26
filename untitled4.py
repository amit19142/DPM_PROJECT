# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t26XfusHJkOoRDncdp5QBM-GJ-wATbvr
"""

import pandas as pd
import numpy as np
import pandas_datareader as pdr
from datetime import datetime
import matplotlib.pyplot as plt

# df = pd.DataFrame({'close':[4724.89, 4378.51,6463.00,9838.96,13716.36,10285.10,
#                           10326.76,6923.91,9246.01,7485.01,6390.07,7730.93,
#                           7011.21,6626.57,6371.93,4041.32,3702.90,3434.10,
#   
#                         3813.69,4103.95,5320.81,8555.00,10854.10]})
def plot4():
    df=pd.read_csv('user.csv')
    print(df)
    n = 14


    def rma(x, n, y0):
        a = (n-1) / n
        ak = a**np.arange(len(x)-1, -1, -1)
        return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]

    df['change'] = df['price'].diff()
    df['gain'] = df.change.mask(df.change < 0, 0.0)
    df['loss'] = -df.change.mask(df.change > 0, -0.0)
    df['avg_gain'] = rma(df.gain[n+1:].to_numpy(), n, np.nansum(df.gain.to_numpy()[:n+1])/n)
    df['avg_loss'] = rma(df.loss[n+1:].to_numpy(), n, np.nansum(df.loss.to_numpy()[:n+1])/n)
    df['rs'] = df.avg_gain / df.avg_loss
    df['rsi_14'] = 100 - (100 / (1 + df.rs))

    
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.get_xaxis().set_visible(False)


    df['price'].plot(ax=ax1)
    ax1.set_ylabel('Price (Rs)')
    df['rsi_14'].plot(ax=ax2)
    ax2.set_ylim(0,100)
    ax2.axhline(30, color='r', linestyle='--')
    ax2.axhline(70, color='r', linestyle='--')
    ax2.set_ylabel('RSI')

    plt.show()
    