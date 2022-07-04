import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator

rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':12})
# Set the font used for MathJax - more on this later
rc('mathtext',**{'default':'regular'})
rc('axes',**{'titlesize': 15})

def load_from_file(filename, delimiter):
    data = np.loadtxt(open(f"data/{filename}", "rb"), delimiter=delimiter, skiprows=0)
    return data[:,0], data[:,1]

def plot_fig(ax, x, y, marker, color, label=''):
    ax.plot(
        x, y,   # data
        marker=marker,     # marker style
        markersize=8,   # marker size
        markerfacecolor=color,   # marker facecolor
        markeredgecolor='black',  # marker edgecolor
        markeredgewidth=2,       # marker edge width
        linestyle='--',            # line style
        color=color,     # line color
        linewidth=3,      # line width
        label=label      # dataset label
    )
