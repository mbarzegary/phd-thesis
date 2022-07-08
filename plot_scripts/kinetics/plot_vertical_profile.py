from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15,6))

x_cp_rt, y_cp_rt = load_from_file("CPMg-HBSS-RT-profile.txt", "\t")
x_cp_37, y_cp_37 = load_from_file("CPMg-HBSS-37-profile.txt", "\t")
x_uhp_rt, y_uhp_rt = load_from_file("UHPMg-HBSS-RT-profile.txt", "\t")
x_uhp_37, y_uhp_37 = load_from_file("UHPMg-HBSS-37-profile.txt", "\t")
x_comp_rt, y_comp_rt = load_from_file("vertical-RT-12.csv", ",", 1)
x_comp_37, y_comp_37 = load_from_file("vertical-37-12.csv", ",", 1)

x_comp_rt = x_comp_rt * 1000 + 50
x_comp_37 = x_comp_37 * 1000 + 50

plot_fig(ax[0], y_cp_rt, x_cp_rt, 's', 'blue', 'RT')
plot_fig(ax[0], y_cp_37, x_cp_37, 'o', 'red', r'37 $^{\circ}$C')
ax[0].set_title("Experiment - CPMg")

plot_fig(ax[1], y_uhp_rt, x_uhp_rt, 's', 'blue', 'RT')
plot_fig(ax[1], y_uhp_37, x_uhp_37, 'o', 'red', r'37$^{\circ}$C')
ax[1].set_title("Experiment - UHPMg")

plot_fig(ax[2], y_comp_rt, x_comp_rt, None, 'blue', 'RT')
plot_fig(ax[2], y_comp_37, x_comp_37, None, 'red', r'37$^{\circ}$C')
ax[2].set_title("Computational results")

# for axes in ax.flat:
for i, axes in enumerate(ax.flat):
    if i == 2:
        axes.set_xlim(7.1, 8.5)
    else:
        axes.set_xlim(7.3, 8.5)
    axes.set_ylim(0, 550)
    axes.invert_xaxis()
    axes.set_xlabel("Local pH")
    axes.set_ylabel("Height ($\mu m$)")
    axes.yaxis.set_major_locator(MultipleLocator(50))
    # axes.yaxis.set_minor_locator(MultipleLocator(50))
    # axes.legend()

handles, labels = ax[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=2)

plt.tight_layout()
fig.subplots_adjust(bottom=0.17)
plt.savefig('vertical_profile.png', dpi=300)
plt.show()
