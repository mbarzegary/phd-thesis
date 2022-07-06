import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator

rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':12})
# Set the font used for MathJax - more on this later
rc('mathtext',**{'default':'regular'})
rc('axes',**{'titlesize': 15})

def load_from_file(filename, delimiter, skiprows=0):
    data = np.loadtxt(open(f"data/{filename}", "rb"), delimiter=delimiter, skiprows=skiprows)
    return data[:,0], data[:,1]

def plot_fig(ax, x, y, marker, color, label='', alpha=1, edgecolor='black', markersize=8):
    ax.plot(
        x, y,   # data
        marker=marker,     # marker style
        markersize=markersize,   # marker size
        markerfacecolor=color,   # marker facecolor
        markeredgecolor=edgecolor,  # marker edgecolor
        markeredgewidth=2,       # marker edge width
        linestyle='-',            # line style
        color=color,     # line color
        linewidth=3,      # line width
        label=label,      # dataset label
        alpha=alpha       # transparency
    )
