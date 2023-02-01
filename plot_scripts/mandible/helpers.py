import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator

rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':12})
# Set the font used for MathJax - more on this later
rc('mathtext',**{'default':'regular'})
rc('axes',**{'titlesize': 15})

def load_from_file(filename, delimiter, index_x, index_y, skip_header, multiplier=1):
    data = np.genfromtxt(open(f"data/{filename}", "rb"), delimiter=delimiter, skip_header=skip_header)
    return data[:, index_x]*multiplier, data[:, index_y]

def load_from_file_all(filename, delimiter, skip_header):
    data = np.genfromtxt(open(f"data/{filename}", "rb"), delimiter=delimiter, skip_header=skip_header)
    return data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4]

def plot_fig(ax, x, y, marker, color, label='', alpha=1, edgecolor='black', markersize=8, linestyle='-'):
    ax.plot(
        x, y,   # data
        marker=marker,     # marker style
        markersize=markersize,   # marker size
        markerfacecolor=color,   # marker facecolor
        markeredgecolor=edgecolor,  # marker edgecolor
        markeredgewidth=1,       # marker edge width
        linestyle=linestyle,            # line style
        color=color,     # line color
        linewidth=3,      # line width
        label=label,      # dataset label
        alpha=alpha       # transparency
    )
