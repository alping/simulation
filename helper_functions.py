import numpy as np
import scipy.stats as sp
import holoviews as hv


def histogram(x, bins=10, **kwargs):
    return hv.Histogram(np.histogram(x, bins=bins), **kwargs)


def barchart(x, **kwargs):
    return hv.Bars(zip(range(x.min(), x.max() + 1),
                       np.bincount(x)[x.min():]), **kwargs)


def scatter(x, y, **kwargs):
    return hv.Scatter((x, y), **kwargs)


def regplot(x, y):
    slope, intercept, r, p, stderr = sp.linregress(x, y)
    line_x = np.linspace(x.min(), x.max())
    line_y = slope * line_x + intercept
    return hv.Scatter((x, y)) * hv.Curve((line_x, line_y)).options(color='red')
