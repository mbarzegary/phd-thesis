import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator

rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':12})
# Set the font used for MathJax - more on this later
rc('mathtext',**{'default':'regular'})
rc('axes',**{'titlesize': 15})

def load_aspect_ratio(filename):
    data = np.loadtxt(open(f"data/{filename}", "rb"), delimiter="\t", skiprows=3,)
    return data[:,1], data[:,2]

def load_gamma(filename):
    data = np.loadtxt(open(f"data/{filename}", "rb"), delimiter=" ", skiprows=0, usecols=range(8))
    return data[:,4], data[:,7]

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

def process_case(case_name):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

    aspect_ratio, aspect_ratio_elements = load_aspect_ratio(f"{case_name}_aspect_ratio_3d.txt")
    gamma, gamma_elements = load_gamma(f"{case_name}_gamma.txt")

    plot_fig(ax[0], aspect_ratio, aspect_ratio_elements, None, 'blue', '', 1.0, None, 5)
    ax[0].set_xlabel("Aspect ratio")

    plot_fig(ax[1], gamma, gamma_elements, None, 'orange', '', 1.0, None, 5)
    ax[1].set_xlabel("Gamma")

    for i, axes in enumerate(ax.flat):
        axes.set_ylabel("Number of elements")
        axes.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        axes.yaxis.major.formatter._useMathText = True

    plt.tight_layout()
    plt.savefig(f'{case_name}_quality.png', dpi=300)
    # plt.show()
