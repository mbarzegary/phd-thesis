from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,6))

x_cp_rt_3h, y_cp_rt_3h = load_from_file("CPMg-HBSS-RT-3h.txt", "\t")
x_cp_rt_6h, y_cp_rt_6h = load_from_file("CPMg-HBSS-RT-6h.txt", "\t")
x_cp_rt_12h, y_cp_rt_12h = load_from_file("CPMg-HBSS-RT-12h.txt", "\t")
x_cp_37_3h, y_cp_37_3h = load_from_file("CPMg-HBSS-37-3h.txt", "\t")
x_cp_37_6h, y_cp_37_6h = load_from_file("CPMg-HBSS-37-6h.txt", "\t")
x_cp_37_12h, y_cp_37_12h = load_from_file("CPMg-HBSS-37-12h.txt", "\t")
x_uhp_rt_3h, y_uhp_rt_3h = load_from_file("UHPMg-HBSS-RT-3h.txt", "\t")
x_uhp_rt_6h, y_uhp_rt_6h = load_from_file("UHPMg-HBSS-RT-6h.txt", "\t")
x_uhp_rt_12h, y_uhp_rt_12h = load_from_file("UHPMg-HBSS-RT-12h.txt", "\t")
x_uhp_37_3h, y_uhp_37_3h = load_from_file("UHPMg-HBSS-37-3h.txt", "\t")
x_uhp_37_6h, y_uhp_37_6h = load_from_file("UHPMg-HBSS-37-6h.txt", "\t")
x_uhp_37_12h, y_uhp_37_12h = load_from_file("UHPMg-HBSS-37-12h.txt", "\t")

plot_fig(ax[0], x_cp_rt_3h, y_cp_rt_3h, 's', 'blue', 'RT-3h', 0.15, 'black', 5)
plot_fig(ax[0], x_cp_rt_6h, y_cp_rt_6h, 's', 'blue', 'RT-6h', 0.4, 'black', 5)
plot_fig(ax[0], x_cp_rt_12h, y_cp_rt_12h, 's', 'blue', 'RT-12h', 1.0, 'black', 5)
plot_fig(ax[0], x_cp_37_3h, y_cp_37_3h, 'o', 'red', r'37$^{\circ}$C-3h', 0.15, 'black', 5)
plot_fig(ax[0], x_cp_37_6h, y_cp_37_6h, 'o', 'red', r'37$^{\circ}$C-6h', 0.4, 'black', 5)
plot_fig(ax[0], x_cp_37_12h, y_cp_37_12h, 'o', 'red', r'37$^{\circ}$C-12h', 1.0, 'black', 5)
ax[0].set_title("CPMg")

plot_fig(ax[1], x_uhp_rt_3h, y_uhp_rt_3h, 's', 'blue', 'RT-3h', 0.15, 'black', 5)
plot_fig(ax[1], x_uhp_rt_6h, y_uhp_rt_6h, 's', 'blue', 'RT-6h', 0.4, 'black', 5)
plot_fig(ax[1], x_uhp_rt_12h, y_uhp_rt_12h, 's', 'blue', 'RT-12h', 1.0, 'black', 5)
plot_fig(ax[1], x_uhp_37_3h, y_uhp_37_3h, 'o', 'red', r'37$^{\circ}$C-3h', 0.15, 'black', 5)
plot_fig(ax[1], x_uhp_37_6h, y_uhp_37_6h, 'o', 'red', r'37$^{\circ}$C-6h', 0.4, 'black', 5)
plot_fig(ax[1], x_uhp_37_12h, y_uhp_37_12h, 'o', 'red', r'37$^{\circ}$C-12h', 1.0, 'black', 5)
ax[1].set_title("UHPMg")

for axes in ax.flat:
    axes.set_ylim(7.3, 8.8)
    axes.set_xlim(-1750, 1750)
    axes.set_ylabel("Local pH")
    axes.set_xlabel("X ($\mu m$)")
    # axes.yaxis.set_major_locator(MultipleLocator(50))
    # axes.yaxis.set_minor_locator(MultipleLocator(50))
    # axes.legend()

handles, labels = ax[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=6)


plt.tight_layout()
fig.subplots_adjust(bottom=0.17)
plt.savefig('reproduce_line_scans.png', dpi=300)
plt.show()
