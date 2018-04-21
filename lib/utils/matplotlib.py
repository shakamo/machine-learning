from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.finance as mpf
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker

ROOT = Path(__file__).parent.resolve().parent.resolve().parent.resolve().joinpath('input')


def show_2d(x, y, z, x_name, y_name):
    # 描画する
    np.where(0 < z)
    plt.scatter(x, y, c=z, vmin=min(z[np.where(0 < z)]), vmax=max(z[np.where(0 < z)]))

    plt.xlabel(x_name)
    plt.ylabel(y_name)

    plt.colorbar()
    plt.show()


def show_3d(a, b, c, y, a_name, b_name, c_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    p = ax.scatter(a, b, c, c=y, vmin=min(y), vmax=max(y))

    ax.set_xlabel(a_name)
    ax.set_ylabel(b_name)
    ax.set_zlabel(c_name)

    fig.colorbar(p)
    plt.show()


def show_line1(x, y):
    plt.plot(y, x)

    plt.show()


def show_line2(x1, x2, y):
    plt.plot(y, x1, label='a')
    plt.plot(y, x2, label='b')

    plt.show()


def show_line3(x1, x2, x3, y):
    plt.plot(y, x1, label='a')
    plt.plot(y, x2, label='b')
    plt.plot(y, x3, label='c')

    plt.legend()

    plt.show()


def show_candlestick(ohlc):
    fig, ax = plt.subplots()

    # ローソク足
    mpf.candlestick2_ohlc(ax, opens=ohlc['1_open'].values, closes=ohlc['4_close'].values,
                          lows=ohlc['3_low'].values, highs=ohlc['2_high'].values,
                          width=0.2, colorup='r', colordown='b')

    # x軸を時間にする
    xdate = ohlc.index
    ax.xaxis.set_major_locator(ticker.MaxNLocator(6))

    f = lambda x, y: mydate(x, ohlc)

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(f))
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

    fig.autofmt_xdate()
    fig.tight_layout()

    plt.show()


def mydate(x, ohlc):
    try:
        return ohlc['0_openTime'].iloc[int(x)]
    except IndexError:
        return ''
